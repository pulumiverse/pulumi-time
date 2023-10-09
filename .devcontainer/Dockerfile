ARG GO_VERSION=1.20.4
FROM golang:${GO_VERSION}-bullseye

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Update apt-get and install various needed utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl xz-utils make git

# Install go linter
ARG GOLANGCI_LINT_VERSION=v1.54.2
RUN mkdir -p "$GOPATH/bin" && \
    curl -sSfL 'https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh' | sh -s -- -b "$GOPATH/bin" ${GOLANGCI_LINT_VERSION}

ENV PATH=$PATH:$GOPATH/bin

# Install pulumictl
ARG PULUMICTL_VERSION=v0.0.44
RUN rm -rf /usr/local/bin/pulumictl && \
    curl -fsSL "https://github.com/pulumi/pulumictl/releases/download/${PULUMICTL_VERSION}/pulumictl-${PULUMICTL_VERSION}-linux-amd64.tar.gz" | \
    tar -C /usr/local/bin -xzf -

# Install nodejs
ARG NODEJS_VERSION=v16.16.0
ARG NODEJS_PKG=node-${NODEJS_VERSION}-linux-x64
ARG NODEJS_TARBALL=${NODEJS_PKG}.tar.xz
RUN rm -rf /usr/local/node && \
    curl -sSfL "https://nodejs.org/dist/${NODEJS_VERSION}/${NODEJS_TARBALL}" | \
    tar -C /usr/local -xJf - && \
    mv /usr/local/${NODEJS_PKG} /usr/local/node

ENV PATH=$PATH:/usr/local/node/bin

# Install yarn
RUN npm install --global yarn

# Install python and related items
RUN apt-get install -y --no-install-recommends python3 python3-setuptools

# Install .NET
RUN source /etc/os-release && \
    curl "https://packages.microsoft.com/config/${ID}/${VERSION_ID}/packages-microsoft-prod.deb" --output packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https dotnet-sdk-6.0

ENV DOTNET_CLI_TELEMETRY_OPTOUT=1

# Install Pulumi
RUN curl -fsSL https://get.pulumi.com | sh
ENV PATH=$PATH:/root/.pulumi/bin

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*
