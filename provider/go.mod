module github.com/pulumiverse/pulumi-time/provider

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220725190814-23001ad6ec03
	github.com/hashicorp/terraform-provider-time/shim => ./shim
)

require (
	github.com/hashicorp/terraform-provider-time/shim v0.0.0-00010101000000-000000000000
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.26.0
	github.com/pulumi/pulumi/sdk/v3 v3.36.0
)
