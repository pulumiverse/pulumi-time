SHELL            := /bin/bash
PROJECT          := github.com/pulumiverse/pulumi-time
NODE_MODULE_NAME := @pulumiverse/time
TF_NAME          := time
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version
PROJECT_DIR      := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

JAVA_GEN         := pulumi-java-gen
JAVA_GEN_VERSION := v0.9.8
TFGEN            := pulumi-tfgen-time
PROVIDER         := pulumi-resource-time
VERSION          := $(shell pulumictl get version)

TESTPARALLELISM  := 4

WORKING_DIR      := $(shell pwd)

GO_MAJOR_VERSION := $(shell go version | cut -c 14- | cut -d' ' -f1 | cut -d'.' -f1)
GO_MINOR_VERSION := $(shell go version | cut -c 14- | cut -d' ' -f1 | cut -d'.' -f2)
####
# Defines the required Go version. This is a safeguard, because
# the (local) version must match the version specified in .github/workflows/release.yml
# otherwise publkishing the Go SDK of the provider will fail
REQUIRED_GO_MAJOR_VERSION := 1
REQUIRED_GO_MINOR_VERSION := 21
GO_VERSION_VALIDATION_ERR_MSG := Golang version $(REQUIRED_GO_MAJOR_VERSION).$(REQUIRED_GO_MINOR_VERSION) is required

.PHONY: development provider build_sdks build_nodejs build_dotnet build_go build_python cleanup validate_go_version

validate_go_version: ## Validates the installed version of go
	@if [ $(GO_MAJOR_VERSION) -ne $(REQUIRED_GO_MAJOR_VERSION) ]; then \
		echo '$(GO_VERSION_VALIDATION_ERR_MSG)';\
		exit 1 ;\
	fi
	@if [ $(GO_MINOR_VERSION) -ne $(REQUIRED_GO_MINOR_VERSION) ]; then \
		echo '$(GO_VERSION_VALIDATION_ERR_MSG)';\
		exit 1 ;\
	fi

development:: install_plugins provider lint_provider build_sdks install_sdks cleanup # Build the provider & SDKs for a development environment

# Required for the codegen action that runs in pulumi/pulumi and pulumi/pulumi-terraform-bridge
build:: install_plugins provider build_sdks install_sdks
only_build:: build

generate::
	go generate provider/resources.go

tfgen:: install_plugins
	(cd provider && go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN})
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	(cd provider && VERSION=$(VERSION) go generate cmd/${PROVIDER}/main.go)

provider:: tfgen install_plugins # build the provider binary
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER})

build_sdks:: install_plugins provider build_nodejs build_python build_go build_dotnet # build all the sdks

build_nodejs:: VERSION := $(shell pulumictl get version --language javascript)
build_nodejs:: install_plugins tfgen # build the node sdk
	$(WORKING_DIR)/bin/$(TFGEN) nodejs --overlays provider/overlays/nodejs --out sdk/nodejs/
	cd sdk/nodejs/ && \
        yarn install && \
        yarn run tsc && \
        cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json

build_python:: PYPI_VERSION := $(shell pulumictl get version --language python)
build_python:: install_plugins tfgen # build the python sdk
	$(WORKING_DIR)/bin/$(TFGEN) python --overlays provider/overlays/python --out sdk/python/
	cd sdk/python/ && \
        cp ../../README.md . && \
        python3 setup.py clean --all 2>/dev/null && \
        rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
        sed -i.bak -e 's/^VERSION = .*/VERSION = "$(PYPI_VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
        rm ./bin/setup.py.bak && \
        cd ./bin && python3 setup.py build sdist

build_dotnet:: DOTNET_VERSION := $(shell pulumictl get version --language dotnet)
build_dotnet:: install_plugins tfgen # build the dotnet sdk
	pulumictl get version --language dotnet
	$(WORKING_DIR)/bin/$(TFGEN) dotnet --overlays provider/overlays/dotnet --out sdk/dotnet/
	cd sdk/dotnet/ && \
		echo "${DOTNET_VERSION}" >version.txt && \
        dotnet build /p:Version=${DOTNET_VERSION}

build_go:: install_plugins tfgen # build the go sdk
	$(WORKING_DIR)/bin/$(TFGEN) go --overlays provider/overlays/go --out sdk/go/
	cd sdk/go/ && \
		go mod tidy

build_java:: PACKAGE_VERSION := $(shell pulumictl get version --language generic)
build_java:: $(WORKING_DIR)/bin/$(JAVA_GEN)
	$(WORKING_DIR)/bin/$(JAVA_GEN) generate --schema provider/cmd/$(PROVIDER)/schema.json --out sdk/java  --build gradle-nexus
	cd sdk/java/ && \
		echo "module fake_java_module // Exclude this directory from Go tools\n\ngo 1.17" > go.mod && \
		gradle --console=plain build

$(WORKING_DIR)/bin/$(JAVA_GEN)::
	$(shell pulumictl download-binary -n pulumi-language-java -v $(JAVA_GEN_VERSION) -r pulumi/pulumi-java)

lint_provider:: provider # lint the provider code
	cd provider && golangci-lint run -c ../.golangci.yml

tidy:: # call go mod tidy in relevant directories
	find ./provider -name go.mod -execdir go mod tidy \;

cleanup:: # cleans up the temporary directory
	rm -r $(WORKING_DIR)/bin
	rm -f provider/cmd/${PROVIDER}/schema.go

help::
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
 	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
 	expand -t20

clean::
	rm -rf sdk/{dotnet,nodejs,go,python,java} sdk/go.sum

.PHONY: fmt
fmt::
	@echo "Fixing source code with gofmt..."
	find . -name '*.go' | grep -v vendor | xargs gofmt -s -w

install_plugins:: validate_go_version
	[ -x $(shell which pulumi) ] || curl -fsSL https://get.pulumi.com | sh
	pulumi plugin install resource random
	pulumi plugin install resource aws
	pulumi plugin install resource null

install_dotnet_sdk::
	mkdir -p $(WORKING_DIR)/nuget
	find . -name '*.nupkg' -print -exec cp -p {} ${WORKING_DIR}/nuget \;

install_python_sdk::

install_go_sdk::

install_nodejs_sdk::
	yarn link --cwd $(WORKING_DIR)/sdk/nodejs/bin

install_sdks:: install_dotnet_sdk install_python_sdk install_nodejs_sdk

test::
	cd examples && go test -v -tags=all -parallel ${TESTPARALLELISM} -timeout 2h

.PHONY: go.work
go.work::
	@cd $(PROJECT_DIR)
ifeq (,$(wildcard $(PROJECT_DIR)/go.work))
	@echo "Initializing go.work..."
	@go work init
else
	@echo "Updating go.work..."
endif
	@go work use provider provider/shim sdk examples
