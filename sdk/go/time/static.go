// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package time

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
// ### Basic Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-time/sdk/go/time"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := time.NewStatic(ctx, "example", nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("currentTime", example.Rfc3339)
//			return nil
//		})
//	}
//
// ```
// ### Triggers Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
//	"github.com/pulumi/pulumi-time/sdk/go/time"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			amiUpdate, err := time.NewStatic(ctx, "amiUpdate", &time.StaticArgs{
//				Triggers: pulumi.StringMap{
//					"ami_id": pulumi.Any(data.Aws_ami.Example.Id),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ec2.NewInstance(ctx, "server", &ec2.InstanceArgs{
//				Ami: amiUpdate.Triggers.ApplyT(func(triggers interface{}) (string, error) {
//					return triggers.AmiId, nil
//				}).(pulumi.StringOutput),
//				Tags: pulumi.StringMap{
//					"AmiUpdateTime": amiUpdate.Rfc3339,
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// This resource can be imported using the UTC RFC3339 value, e.g.
//
// ```sh
//
//	$ pulumi import time:index/static:Static example 2020-02-12T06:36:13Z
//
// ```
//
//	The `triggers` argument cannot be imported.
type Static struct {
	pulumi.CustomResourceState

	// Number day of timestamp.
	Day pulumi.IntOutput `pulumi:"day"`
	// Number hour of timestamp.
	Hour pulumi.IntOutput `pulumi:"hour"`
	// Number minute of timestamp.
	Minute pulumi.IntOutput `pulumi:"minute"`
	// Number month of timestamp.
	Month pulumi.IntOutput `pulumi:"month"`
	// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
	// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
	Rfc3339 pulumi.StringOutput `pulumi:"rfc3339"`
	// Number second of timestamp.
	Second pulumi.IntOutput `pulumi:"second"`
	// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
	// documentation](../index.md) for more information.
	Triggers pulumi.StringMapOutput `pulumi:"triggers"`
	// Number of seconds since epoch time, e.g. `1581489373`.
	Unix pulumi.IntOutput `pulumi:"unix"`
	// Number year of timestamp.
	Year pulumi.IntOutput `pulumi:"year"`
}

// NewStatic registers a new resource with the given unique name, arguments, and options.
func NewStatic(ctx *pulumi.Context,
	name string, args *StaticArgs, opts ...pulumi.ResourceOption) (*Static, error) {
	if args == nil {
		args = &StaticArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource Static
	err := ctx.RegisterResource("time:index/static:Static", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStatic gets an existing Static resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStatic(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StaticState, opts ...pulumi.ResourceOption) (*Static, error) {
	var resource Static
	err := ctx.ReadResource("time:index/static:Static", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Static resources.
type staticState struct {
	// Number day of timestamp.
	Day *int `pulumi:"day"`
	// Number hour of timestamp.
	Hour *int `pulumi:"hour"`
	// Number minute of timestamp.
	Minute *int `pulumi:"minute"`
	// Number month of timestamp.
	Month *int `pulumi:"month"`
	// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
	// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
	Rfc3339 *string `pulumi:"rfc3339"`
	// Number second of timestamp.
	Second *int `pulumi:"second"`
	// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
	// documentation](../index.md) for more information.
	Triggers map[string]string `pulumi:"triggers"`
	// Number of seconds since epoch time, e.g. `1581489373`.
	Unix *int `pulumi:"unix"`
	// Number year of timestamp.
	Year *int `pulumi:"year"`
}

type StaticState struct {
	// Number day of timestamp.
	Day pulumi.IntPtrInput
	// Number hour of timestamp.
	Hour pulumi.IntPtrInput
	// Number minute of timestamp.
	Minute pulumi.IntPtrInput
	// Number month of timestamp.
	Month pulumi.IntPtrInput
	// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
	// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
	Rfc3339 pulumi.StringPtrInput
	// Number second of timestamp.
	Second pulumi.IntPtrInput
	// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
	// documentation](../index.md) for more information.
	Triggers pulumi.StringMapInput
	// Number of seconds since epoch time, e.g. `1581489373`.
	Unix pulumi.IntPtrInput
	// Number year of timestamp.
	Year pulumi.IntPtrInput
}

func (StaticState) ElementType() reflect.Type {
	return reflect.TypeOf((*staticState)(nil)).Elem()
}

type staticArgs struct {
	// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
	// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
	Rfc3339 *string `pulumi:"rfc3339"`
	// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
	// documentation](../index.md) for more information.
	Triggers map[string]string `pulumi:"triggers"`
}

// The set of arguments for constructing a Static resource.
type StaticArgs struct {
	// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
	// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
	Rfc3339 pulumi.StringPtrInput
	// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
	// documentation](../index.md) for more information.
	Triggers pulumi.StringMapInput
}

func (StaticArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*staticArgs)(nil)).Elem()
}

type StaticInput interface {
	pulumi.Input

	ToStaticOutput() StaticOutput
	ToStaticOutputWithContext(ctx context.Context) StaticOutput
}

func (*Static) ElementType() reflect.Type {
	return reflect.TypeOf((**Static)(nil)).Elem()
}

func (i *Static) ToStaticOutput() StaticOutput {
	return i.ToStaticOutputWithContext(context.Background())
}

func (i *Static) ToStaticOutputWithContext(ctx context.Context) StaticOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StaticOutput)
}

// StaticArrayInput is an input type that accepts StaticArray and StaticArrayOutput values.
// You can construct a concrete instance of `StaticArrayInput` via:
//
//	StaticArray{ StaticArgs{...} }
type StaticArrayInput interface {
	pulumi.Input

	ToStaticArrayOutput() StaticArrayOutput
	ToStaticArrayOutputWithContext(context.Context) StaticArrayOutput
}

type StaticArray []StaticInput

func (StaticArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Static)(nil)).Elem()
}

func (i StaticArray) ToStaticArrayOutput() StaticArrayOutput {
	return i.ToStaticArrayOutputWithContext(context.Background())
}

func (i StaticArray) ToStaticArrayOutputWithContext(ctx context.Context) StaticArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StaticArrayOutput)
}

// StaticMapInput is an input type that accepts StaticMap and StaticMapOutput values.
// You can construct a concrete instance of `StaticMapInput` via:
//
//	StaticMap{ "key": StaticArgs{...} }
type StaticMapInput interface {
	pulumi.Input

	ToStaticMapOutput() StaticMapOutput
	ToStaticMapOutputWithContext(context.Context) StaticMapOutput
}

type StaticMap map[string]StaticInput

func (StaticMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Static)(nil)).Elem()
}

func (i StaticMap) ToStaticMapOutput() StaticMapOutput {
	return i.ToStaticMapOutputWithContext(context.Background())
}

func (i StaticMap) ToStaticMapOutputWithContext(ctx context.Context) StaticMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StaticMapOutput)
}

type StaticOutput struct{ *pulumi.OutputState }

func (StaticOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Static)(nil)).Elem()
}

func (o StaticOutput) ToStaticOutput() StaticOutput {
	return o
}

func (o StaticOutput) ToStaticOutputWithContext(ctx context.Context) StaticOutput {
	return o
}

// Number day of timestamp.
func (o StaticOutput) Day() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Day }).(pulumi.IntOutput)
}

// Number hour of timestamp.
func (o StaticOutput) Hour() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Hour }).(pulumi.IntOutput)
}

// Number minute of timestamp.
func (o StaticOutput) Minute() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Minute }).(pulumi.IntOutput)
}

// Number month of timestamp.
func (o StaticOutput) Month() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Month }).(pulumi.IntOutput)
}

// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
func (o StaticOutput) Rfc3339() pulumi.StringOutput {
	return o.ApplyT(func(v *Static) pulumi.StringOutput { return v.Rfc3339 }).(pulumi.StringOutput)
}

// Number second of timestamp.
func (o StaticOutput) Second() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Second }).(pulumi.IntOutput)
}

// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider
// documentation](../index.md) for more information.
func (o StaticOutput) Triggers() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Static) pulumi.StringMapOutput { return v.Triggers }).(pulumi.StringMapOutput)
}

// Number of seconds since epoch time, e.g. `1581489373`.
func (o StaticOutput) Unix() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Unix }).(pulumi.IntOutput)
}

// Number year of timestamp.
func (o StaticOutput) Year() pulumi.IntOutput {
	return o.ApplyT(func(v *Static) pulumi.IntOutput { return v.Year }).(pulumi.IntOutput)
}

type StaticArrayOutput struct{ *pulumi.OutputState }

func (StaticArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Static)(nil)).Elem()
}

func (o StaticArrayOutput) ToStaticArrayOutput() StaticArrayOutput {
	return o
}

func (o StaticArrayOutput) ToStaticArrayOutputWithContext(ctx context.Context) StaticArrayOutput {
	return o
}

func (o StaticArrayOutput) Index(i pulumi.IntInput) StaticOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Static {
		return vs[0].([]*Static)[vs[1].(int)]
	}).(StaticOutput)
}

type StaticMapOutput struct{ *pulumi.OutputState }

func (StaticMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Static)(nil)).Elem()
}

func (o StaticMapOutput) ToStaticMapOutput() StaticMapOutput {
	return o
}

func (o StaticMapOutput) ToStaticMapOutputWithContext(ctx context.Context) StaticMapOutput {
	return o
}

func (o StaticMapOutput) MapIndex(k pulumi.StringInput) StaticOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Static {
		return vs[0].(map[string]*Static)[vs[1].(string)]
	}).(StaticOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StaticInput)(nil)).Elem(), &Static{})
	pulumi.RegisterInputType(reflect.TypeOf((*StaticArrayInput)(nil)).Elem(), StaticArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*StaticMapInput)(nil)).Elem(), StaticMap{})
	pulumi.RegisterOutputType(StaticOutput{})
	pulumi.RegisterOutputType(StaticArrayOutput{})
	pulumi.RegisterOutputType(StaticMapOutput{})
}
