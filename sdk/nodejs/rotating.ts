// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 * ### Basic Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as time from "@pulumi/time";
 *
 * const example = new time.Rotating("example", {
 *     rotationDays: 30,
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported using the base UTC RFC3339 value and rotation years, months, days, hours, and minutes, separated by commas (`,`), e.g. for 30 days
 *
 * ```sh
 *  $ pulumi import time:index/rotating:Rotating example 2020-02-12T06:36:13Z,0,0,30,0,0
 * ```
 *
 *  Otherwise, to import with the rotation RFC3339 value, the base UTC RFC3339 value and rotation UTC RFC3339 value, separated by commas (`,`), e.g.
 *
 * ```sh
 *  $ pulumi import time:index/rotating:Rotating example 2020-02-12T06:36:13Z,2020-02-13T06:36:13Z
 * ```
 *
 *  The `triggers` argument cannot be imported.
 */
export class Rotating extends pulumi.CustomResource {
    /**
     * Get an existing Rotating resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RotatingState, opts?: pulumi.CustomResourceOptions): Rotating {
        return new Rotating(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'time:index/rotating:Rotating';

    /**
     * Returns true if the given object is an instance of Rotating.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rotating {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rotating.__pulumiType;
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
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
     * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    public readonly rfc3339!: pulumi.Output<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationDays!: pulumi.Output<number | undefined>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationHours!: pulumi.Output<number | undefined>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationMinutes!: pulumi.Output<number | undefined>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationMonths!: pulumi.Output<number | undefined>;
    /**
     * Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
     * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
     * least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationRfc3339!: pulumi.Output<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    public readonly rotationYears!: pulumi.Output<number | undefined>;
    /**
     * Number second of timestamp.
     */
    public /*out*/ readonly second!: pulumi.Output<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
     * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
     * more information.
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
     * Create a Rotating resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RotatingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RotatingArgs | RotatingState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RotatingState | undefined;
            resourceInputs["day"] = state ? state.day : undefined;
            resourceInputs["hour"] = state ? state.hour : undefined;
            resourceInputs["minute"] = state ? state.minute : undefined;
            resourceInputs["month"] = state ? state.month : undefined;
            resourceInputs["rfc3339"] = state ? state.rfc3339 : undefined;
            resourceInputs["rotationDays"] = state ? state.rotationDays : undefined;
            resourceInputs["rotationHours"] = state ? state.rotationHours : undefined;
            resourceInputs["rotationMinutes"] = state ? state.rotationMinutes : undefined;
            resourceInputs["rotationMonths"] = state ? state.rotationMonths : undefined;
            resourceInputs["rotationRfc3339"] = state ? state.rotationRfc3339 : undefined;
            resourceInputs["rotationYears"] = state ? state.rotationYears : undefined;
            resourceInputs["second"] = state ? state.second : undefined;
            resourceInputs["triggers"] = state ? state.triggers : undefined;
            resourceInputs["unix"] = state ? state.unix : undefined;
            resourceInputs["year"] = state ? state.year : undefined;
        } else {
            const args = argsOrState as RotatingArgs | undefined;
            resourceInputs["rfc3339"] = args ? args.rfc3339 : undefined;
            resourceInputs["rotationDays"] = args ? args.rotationDays : undefined;
            resourceInputs["rotationHours"] = args ? args.rotationHours : undefined;
            resourceInputs["rotationMinutes"] = args ? args.rotationMinutes : undefined;
            resourceInputs["rotationMonths"] = args ? args.rotationMonths : undefined;
            resourceInputs["rotationRfc3339"] = args ? args.rotationRfc3339 : undefined;
            resourceInputs["rotationYears"] = args ? args.rotationYears : undefined;
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
        super(Rotating.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Rotating resources.
 */
export interface RotatingState {
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
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
     * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationDays?: pulumi.Input<number>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationHours?: pulumi.Input<number>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationMinutes?: pulumi.Input<number>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationMonths?: pulumi.Input<number>;
    /**
     * Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
     * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
     * least one of the 'rotation_' arguments must be configured.
     */
    rotationRfc3339?: pulumi.Input<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationYears?: pulumi.Input<number>;
    /**
     * Number second of timestamp.
     */
    second?: pulumi.Input<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
     * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
     * more information.
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
 * The set of arguments for constructing a Rotating resource.
 */
export interface RotatingArgs {
    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
     * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationDays?: pulumi.Input<number>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationHours?: pulumi.Input<number>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationMinutes?: pulumi.Input<number>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationMonths?: pulumi.Input<number>;
    /**
     * Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
     * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
     * least one of the 'rotation_' arguments must be configured.
     */
    rotationRfc3339?: pulumi.Input<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
     */
    rotationYears?: pulumi.Input<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
     * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
     * more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
