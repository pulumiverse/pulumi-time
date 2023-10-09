// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 * ### Delay Create Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as _null from "@pulumi/null";
 * import * as time from "@pulumiverse/time";
 *
 * // This resource will destroy (potentially immediately) after null_resource.next
 * const previous = new _null.Resource("previous", {});
 * const wait30Seconds = new time.Sleep("wait30Seconds", {createDuration: "30s"}, {
 *     dependsOn: [previous],
 * });
 * // This resource will create (at least) 30 seconds after null_resource.previous
 * const next = new _null.Resource("next", {}, {
 *     dependsOn: [wait30Seconds],
 * });
 * ```
 * ### Delay Destroy Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as _null from "@pulumi/null";
 * import * as time from "@pulumiverse/time";
 *
 * // This resource will destroy (at least) 30 seconds after null_resource.next
 * const previous = new _null.Resource("previous", {});
 * const wait30Seconds = new time.Sleep("wait30Seconds", {destroyDuration: "30s"}, {
 *     dependsOn: [previous],
 * });
 * // This resource will create (potentially immediately) after null_resource.previous
 * const next = new _null.Resource("next", {}, {
 *     dependsOn: [wait30Seconds],
 * });
 * ```
 * ### Triggers Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as time from "@pulumiverse/time";
 *
 * const exampleResourceAssociation = new aws.ram.ResourceAssociation("exampleResourceAssociation", {
 *     resourceArn: aws_subnet.example.arn,
 *     resourceShareArn: aws_ram_resource_share.example.arn,
 * });
 * // AWS resources shared via Resource Access Manager can take a few seconds to
 * // propagate across AWS accounts after RAM returns a successful association.
 * const ramResourcePropagation = new time.Sleep("ramResourcePropagation", {
 *     createDuration: "60s",
 *     triggers: {
 *         subnet_arn: exampleResourceAssociation.resourceArn,
 *         subnet_id: aws_subnet.example.id,
 *     },
 * });
 * const exampleSubnetGroup = new aws.rds.SubnetGroup("exampleSubnetGroup", {subnetIds: [ramResourcePropagation.triggers.apply(triggers => triggers?.subnet_id)]});
 * ```
 *
 * ## Import
 *
 * This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`). e.g. For 30 seconds create duration with no destroy duration
 *
 * ```sh
 *  $ pulumi import time:index/sleep:Sleep example 30s,
 * ```
 *
 *  e.g. For 30 seconds destroy duration with no create duration
 *
 * ```sh
 *  $ pulumi import time:index/sleep:Sleep example ,30s
 * ```
 *
 *  The `triggers` argument cannot be imported.
 */
export class Sleep extends pulumi.CustomResource {
    /**
     * Get an existing Sleep resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SleepState, opts?: pulumi.CustomResourceOptions): Sleep {
        return new Sleep(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'time:index/sleep:Sleep';

    /**
     * Returns true if the given object is an instance of Sleep.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Sleep {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Sleep.__pulumiType;
    }

    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
     */
    public readonly createDuration!: pulumi.Output<string | undefined>;
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
     * or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
     * successfully applied into the Terraform state before destroying this resource to take effect.
     */
    public readonly destroyDuration!: pulumi.Output<string | undefined>;
    /**
     * (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
     */
    public readonly triggers!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Sleep resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SleepArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SleepArgs | SleepState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SleepState | undefined;
            resourceInputs["createDuration"] = state ? state.createDuration : undefined;
            resourceInputs["destroyDuration"] = state ? state.destroyDuration : undefined;
            resourceInputs["triggers"] = state ? state.triggers : undefined;
        } else {
            const args = argsOrState as SleepArgs | undefined;
            resourceInputs["createDuration"] = args ? args.createDuration : undefined;
            resourceInputs["destroyDuration"] = args ? args.destroyDuration : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Sleep.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Sleep resources.
 */
export interface SleepState {
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
     */
    createDuration?: pulumi.Input<string>;
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
     * or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
     * successfully applied into the Terraform state before destroying this resource to take effect.
     */
    destroyDuration?: pulumi.Input<string>;
    /**
     * (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Sleep resource.
 */
export interface SleepArgs {
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
     */
    createDuration?: pulumi.Input<string>;
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
     * or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
     * successfully applied into the Terraform state before destroying this resource to take effect.
     */
    destroyDuration?: pulumi.Input<string>;
    /**
     * (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}