// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ### Basic Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as time from "@pulumiverse/time";
 *
 * const example = new time.Static("example", {});
 * export const currentTime = example.rfc3339;
 * ```
 *
 * ### Triggers Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as time from "@pulumiverse/time";
 *
 * const amiUpdate = new time.Static("amiUpdate", {triggers: {
 *     ami_id: data.aws_ami.example.id,
 * }});
 * const server = new aws.ec2.Instance("server", {
 *     ami: amiUpdate.triggers.apply(triggers => triggers?.amiId),
 *     tags: {
 *         AmiUpdateTime: amiUpdate.rfc3339,
 *     },
 * });
 * // ... (other aws_instance arguments) ...
 * ```
 *
 * ## Import
 *
 * This resource can be imported using the UTC RFC3339 value, e.g.
 *
 * ```sh
 * $ pulumi import time:index/static:Static example 2020-02-12T06:36:13Z
 * ```
 *
 * The `triggers` argument cannot be imported.
 */
export class Static extends pulumi.CustomResource {
    /**
     * Get an existing Static resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StaticState, opts?: pulumi.CustomResourceOptions): Static {
        return new Static(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'time:index/static:Static';

    /**
     * Returns true if the given object is an instance of Static.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Static {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Static.__pulumiType;
    }

    /**
     * Number day of timestamp.
     */
    public /*out*/ readonly day!: pulumi.Output<number>;
    /**
     * Number hour of timestamp.
     */
    public /*out*/ readonly hour!: pulumi.Output<number>;
    /**
     * Number minute of timestamp.
     */
    public /*out*/ readonly minute!: pulumi.Output<number>;
    /**
     * Number month of timestamp.
     */
    public /*out*/ readonly month!: pulumi.Output<number>;
    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    public readonly rfc3339!: pulumi.Output<string>;
    /**
     * Number second of timestamp.
     */
    public /*out*/ readonly second!: pulumi.Output<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
     */
    public readonly triggers!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Number of seconds since epoch time, e.g. `1581489373`.
     */
    public /*out*/ readonly unix!: pulumi.Output<number>;
    /**
     * Number year of timestamp.
     */
    public /*out*/ readonly year!: pulumi.Output<number>;

    /**
     * Create a Static resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: StaticArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StaticArgs | StaticState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as StaticState | undefined;
            resourceInputs["day"] = state ? state.day : undefined;
            resourceInputs["hour"] = state ? state.hour : undefined;
            resourceInputs["minute"] = state ? state.minute : undefined;
            resourceInputs["month"] = state ? state.month : undefined;
            resourceInputs["rfc3339"] = state ? state.rfc3339 : undefined;
            resourceInputs["second"] = state ? state.second : undefined;
            resourceInputs["triggers"] = state ? state.triggers : undefined;
            resourceInputs["unix"] = state ? state.unix : undefined;
            resourceInputs["year"] = state ? state.year : undefined;
        } else {
            const args = argsOrState as StaticArgs | undefined;
            resourceInputs["rfc3339"] = args ? args.rfc3339 : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
            resourceInputs["day"] = undefined /*out*/;
            resourceInputs["hour"] = undefined /*out*/;
            resourceInputs["minute"] = undefined /*out*/;
            resourceInputs["month"] = undefined /*out*/;
            resourceInputs["second"] = undefined /*out*/;
            resourceInputs["unix"] = undefined /*out*/;
            resourceInputs["year"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Static.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Static resources.
 */
export interface StaticState {
    /**
     * Number day of timestamp.
     */
    day?: pulumi.Input<number>;
    /**
     * Number hour of timestamp.
     */
    hour?: pulumi.Input<number>;
    /**
     * Number minute of timestamp.
     */
    minute?: pulumi.Input<number>;
    /**
     * Number month of timestamp.
     */
    month?: pulumi.Input<number>;
    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Number second of timestamp.
     */
    second?: pulumi.Input<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Number of seconds since epoch time, e.g. `1581489373`.
     */
    unix?: pulumi.Input<number>;
    /**
     * Number year of timestamp.
     */
    year?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Static resource.
 */
export interface StaticArgs {
    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
