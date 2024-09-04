// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package time

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-time/sdk/go/time/internal"
)

// ## Example Usage
//
// ### Delay Create Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-null/sdk/go/null"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-time/sdk/go/time"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// This resource will destroy (potentially immediately) after null_resource.next
//			previous, err := null.NewResource(ctx, "previous", nil)
//			if err != nil {
//				return err
//			}
//			wait30Seconds, err := time.NewSleep(ctx, "wait30Seconds", &time.SleepArgs{
//				CreateDuration: pulumi.String("30s"),
//			}, pulumi.DependsOn([]pulumi.Resource{
//				previous,
//			}))
//			if err != nil {
//				return err
//			}
//			// This resource will create (at least) 30 seconds after null_resource.previous
//			_, err = null.NewResource(ctx, "next", nil, pulumi.DependsOn([]pulumi.Resource{
//				wait30Seconds,
//			}))
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ### Delay Destroy Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-null/sdk/go/null"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-time/sdk/go/time"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// This resource will destroy (at least) 30 seconds after null_resource.next
//			previous, err := null.NewResource(ctx, "previous", nil)
//			if err != nil {
//				return err
//			}
//			wait30Seconds, err := time.NewSleep(ctx, "wait30Seconds", &time.SleepArgs{
//				DestroyDuration: pulumi.String("30s"),
//			}, pulumi.DependsOn([]pulumi.Resource{
//				previous,
//			}))
//			if err != nil {
//				return err
//			}
//			// This resource will create (potentially immediately) after null_resource.previous
//			_, err = null.NewResource(ctx, "next", nil, pulumi.DependsOn([]pulumi.Resource{
//				wait30Seconds,
//			}))
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ### Triggers Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ram"
//	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/rds"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-time/sdk/go/time"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleResourceAssociation, err := ram.NewResourceAssociation(ctx, "exampleResourceAssociation", &ram.ResourceAssociationArgs{
//				ResourceArn:      pulumi.Any(aws_subnet.Example.Arn),
//				ResourceShareArn: pulumi.Any(aws_ram_resource_share.Example.Arn),
//			})
//			if err != nil {
//				return err
//			}
//			// AWS resources shared via Resource Access Manager can take a few seconds to
//			// propagate across AWS accounts after RAM returns a successful association.
//			ramResourcePropagation, err := time.NewSleep(ctx, "ramResourcePropagation", &time.SleepArgs{
//				CreateDuration: pulumi.String("60s"),
//				Triggers: pulumi.StringMap{
//					"subnet_arn": exampleResourceAssociation.ResourceArn,
//					"subnet_id":  pulumi.Any(aws_subnet.Example.Id),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = rds.NewSubnetGroup(ctx, "exampleSubnetGroup", &rds.SubnetGroupArgs{
//				SubnetIds: pulumi.StringArray{
//					pulumi.String(ramResourcePropagation.Triggers.ApplyT(func(triggers map[string]string) (*string, error) {
//						return &triggers.Subnet_id, nil
//					}).(pulumi.StringPtrOutput)),
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
// This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`).
//
// e.g. For 30 seconds create duration with no destroy duration:
//
// ```sh
// $ pulumi import time:index/sleep:Sleep example 30s,
// ```
//
// e.g. For 30 seconds destroy duration with no create duration:
//
// ```sh
// $ pulumi import time:index/sleep:Sleep example ,30s
// ```
//
// The `triggers` argument cannot be imported.
type Sleep struct {
	pulumi.CustomResourceState

	// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
	CreateDuration  pulumi.StringPtrOutput `pulumi:"createDuration"`
	DestroyDuration pulumi.StringPtrOutput `pulumi:"destroyDuration"`
	// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
	Triggers pulumi.StringMapOutput `pulumi:"triggers"`
}

// NewSleep registers a new resource with the given unique name, arguments, and options.
func NewSleep(ctx *pulumi.Context,
	name string, args *SleepArgs, opts ...pulumi.ResourceOption) (*Sleep, error) {
	if args == nil {
		args = &SleepArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Sleep
	err := ctx.RegisterResource("time:index/sleep:Sleep", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSleep gets an existing Sleep resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSleep(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SleepState, opts ...pulumi.ResourceOption) (*Sleep, error) {
	var resource Sleep
	err := ctx.ReadResource("time:index/sleep:Sleep", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Sleep resources.
type sleepState struct {
	// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
	CreateDuration  *string `pulumi:"createDuration"`
	DestroyDuration *string `pulumi:"destroyDuration"`
	// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
	Triggers map[string]string `pulumi:"triggers"`
}

type SleepState struct {
	// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
	CreateDuration  pulumi.StringPtrInput
	DestroyDuration pulumi.StringPtrInput
	// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
	Triggers pulumi.StringMapInput
}

func (SleepState) ElementType() reflect.Type {
	return reflect.TypeOf((*sleepState)(nil)).Elem()
}

type sleepArgs struct {
	// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
	CreateDuration  *string `pulumi:"createDuration"`
	DestroyDuration *string `pulumi:"destroyDuration"`
	// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
	Triggers map[string]string `pulumi:"triggers"`
}

// The set of arguments for constructing a Sleep resource.
type SleepArgs struct {
	// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
	CreateDuration  pulumi.StringPtrInput
	DestroyDuration pulumi.StringPtrInput
	// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
	Triggers pulumi.StringMapInput
}

func (SleepArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sleepArgs)(nil)).Elem()
}

type SleepInput interface {
	pulumi.Input

	ToSleepOutput() SleepOutput
	ToSleepOutputWithContext(ctx context.Context) SleepOutput
}

func (*Sleep) ElementType() reflect.Type {
	return reflect.TypeOf((**Sleep)(nil)).Elem()
}

func (i *Sleep) ToSleepOutput() SleepOutput {
	return i.ToSleepOutputWithContext(context.Background())
}

func (i *Sleep) ToSleepOutputWithContext(ctx context.Context) SleepOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SleepOutput)
}

// SleepArrayInput is an input type that accepts SleepArray and SleepArrayOutput values.
// You can construct a concrete instance of `SleepArrayInput` via:
//
//	SleepArray{ SleepArgs{...} }
type SleepArrayInput interface {
	pulumi.Input

	ToSleepArrayOutput() SleepArrayOutput
	ToSleepArrayOutputWithContext(context.Context) SleepArrayOutput
}

type SleepArray []SleepInput

func (SleepArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Sleep)(nil)).Elem()
}

func (i SleepArray) ToSleepArrayOutput() SleepArrayOutput {
	return i.ToSleepArrayOutputWithContext(context.Background())
}

func (i SleepArray) ToSleepArrayOutputWithContext(ctx context.Context) SleepArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SleepArrayOutput)
}

// SleepMapInput is an input type that accepts SleepMap and SleepMapOutput values.
// You can construct a concrete instance of `SleepMapInput` via:
//
//	SleepMap{ "key": SleepArgs{...} }
type SleepMapInput interface {
	pulumi.Input

	ToSleepMapOutput() SleepMapOutput
	ToSleepMapOutputWithContext(context.Context) SleepMapOutput
}

type SleepMap map[string]SleepInput

func (SleepMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Sleep)(nil)).Elem()
}

func (i SleepMap) ToSleepMapOutput() SleepMapOutput {
	return i.ToSleepMapOutputWithContext(context.Background())
}

func (i SleepMap) ToSleepMapOutputWithContext(ctx context.Context) SleepMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SleepMapOutput)
}

type SleepOutput struct{ *pulumi.OutputState }

func (SleepOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Sleep)(nil)).Elem()
}

func (o SleepOutput) ToSleepOutput() SleepOutput {
	return o
}

func (o SleepOutput) ToSleepOutputWithContext(ctx context.Context) SleepOutput {
	return o
}

// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
func (o SleepOutput) CreateDuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Sleep) pulumi.StringPtrOutput { return v.CreateDuration }).(pulumi.StringPtrOutput)
}

func (o SleepOutput) DestroyDuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Sleep) pulumi.StringPtrOutput { return v.DestroyDuration }).(pulumi.StringPtrOutput)
}

// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
func (o SleepOutput) Triggers() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Sleep) pulumi.StringMapOutput { return v.Triggers }).(pulumi.StringMapOutput)
}

type SleepArrayOutput struct{ *pulumi.OutputState }

func (SleepArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Sleep)(nil)).Elem()
}

func (o SleepArrayOutput) ToSleepArrayOutput() SleepArrayOutput {
	return o
}

func (o SleepArrayOutput) ToSleepArrayOutputWithContext(ctx context.Context) SleepArrayOutput {
	return o
}

func (o SleepArrayOutput) Index(i pulumi.IntInput) SleepOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Sleep {
		return vs[0].([]*Sleep)[vs[1].(int)]
	}).(SleepOutput)
}

type SleepMapOutput struct{ *pulumi.OutputState }

func (SleepMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Sleep)(nil)).Elem()
}

func (o SleepMapOutput) ToSleepMapOutput() SleepMapOutput {
	return o
}

func (o SleepMapOutput) ToSleepMapOutputWithContext(ctx context.Context) SleepMapOutput {
	return o
}

func (o SleepMapOutput) MapIndex(k pulumi.StringInput) SleepOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Sleep {
		return vs[0].(map[string]*Sleep)[vs[1].(string)]
	}).(SleepOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SleepInput)(nil)).Elem(), &Sleep{})
	pulumi.RegisterInputType(reflect.TypeOf((*SleepArrayInput)(nil)).Elem(), SleepArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SleepMapInput)(nil)).Elem(), SleepMap{})
	pulumi.RegisterOutputType(SleepOutput{})
	pulumi.RegisterOutputType(SleepArrayOutput{})
	pulumi.RegisterOutputType(SleepMapOutput{})
}
