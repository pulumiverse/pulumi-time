// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package time

import (
	"fmt"
	"path/filepath"
	"strings"
	"unicode"

	"github.com/ettle/strcase"
	shimprovider "github.com/hashicorp/terraform-provider-time/shim"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
	"github.com/pulumiverse/pulumi-time/provider/pkg/version"
)

// all of the token components used below.
const (
	// modules:
	mainMod = "index" // the time module
)

var module_overrides = map[string]string{}

func convertName(tfname string) (module string, name string) {
	tfNameItems := strings.Split(tfname, "_")
	contract.Assertf(len(tfNameItems) >= 2, "Invalid snake case name %s", tfname)
	contract.Assertf(tfNameItems[0] == "time", "Invalid snake case name %s. Does not start with time", tfname)
	if len(tfNameItems) == 2 {
		module = mainMod
		name = tfNameItems[1]
	} else {
		module = tfNameItems[1]
		name = strings.Join(tfNameItems[2:], "_")
	}
	if v, ok := module_overrides[module]; ok {
		module = v
	}
	contract.Assertf(!unicode.IsDigit(rune(name[0])), "Pulumi name must not start with a digit: %s", name)
	name = strcase.ToPascal(name)
	return
}

func makeDataSource(ds string) tokens.ModuleMember {
	mod, name := convertName(ds)
	return tfbridge.MakeDataSource("time", mod, "get"+name)
}

func makeResource(res string) tokens.Type {
	mod, name := convertName(res)
	return tfbridge.MakeResource("time", mod, name)
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(shimprovider.NewProvider())
	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "time",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "Time",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "pulumiverse",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "https://raw.githubusercontent.com/pulumiverse/pulumi-time/main/docs/clock-svgrepo-com.png",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "github://api.github.com/pulumiverse/pulumi-time",
		Description:       "A Pulumi package for creating and managing Time resources",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords: []string{
			"pulumi",
			"time",
			"category/utility",
		},
		License:    "Apache-2.0",
		Homepage:   "https://github.com/pulumiverse/pulumi-time",
		Repository: "https://github.com/pulumiverse/pulumi-time",
		// The GitHub Org for the provider - defaults to `terraform-providers`. Note that this
		// should match the TF provider module's require directive, not any replace directives.
		GitHubOrg: "hashicorp",
		Config:    map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: tfbridge.MakeResource(mainPkg, mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType(mainPkg, "Tags")},
			// 	},
			// },
			"time_offset": {
				Tok: makeResource("time_offset"),
				Docs: &tfbridge.DocInfo{
					Source: "offset.html.markdown",
				},
			},
			"time_rotating": {
				Tok: makeResource("time_rotating"),
				Docs: &tfbridge.DocInfo{
					Source: "rotating.html.markdown",
				},
			},
			"time_static": {
				Tok: makeResource("time_static"),
				Docs: &tfbridge.DocInfo{
					Source: "static.html.markdown",
				},
			},
		},
		IgnoreMappings: []string{
			// time_sleep not mapped because Pulumi provides other means to pause for a specific timespan
			"time_sleep",
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAmi")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@pulumiverse/time",

			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "pulumiverse_time",

			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", "time"),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				"time",
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "Pulumiverse",

			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
		Java: &tfbridge.JavaInfo{
			BasePackage: "com.pulumiverse",
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
