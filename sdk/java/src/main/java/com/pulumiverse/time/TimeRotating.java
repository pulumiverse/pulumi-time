// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumiverse.time;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumiverse.time.TimeRotatingArgs;
import com.pulumiverse.time.Utilities;
import com.pulumiverse.time.inputs.TimeRotatingState;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * 
 * This example configuration will rotate (destroy/create) the resource every 30 days.
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.time.TimeRotating;
 * import com.pulumi.time.TimeRotatingArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var example = new TimeRotating(&#34;example&#34;, TimeRotatingArgs.builder()        
 *             .rotationDays(30)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * This resource can be imported using the base UTC RFC3339 value and rotation years, months, days, hours, and minutes, separated by commas (`,`), e.g. for 30 days console
 * 
 * ```sh
 *  $ pulumi import time:index/timeRotating:TimeRotating example 2020-02-12T06:36:13Z,0,0,30,0,0
 * ```
 * 
 *  Otherwise, to import with the rotation RFC3339 value, the base UTC RFC3339 value and rotation UTC RFC3339 value, separated by commas (`,`), e.g. console
 * 
 * ```sh
 *  $ pulumi import time:index/timeRotating:TimeRotating example 2020-02-12T06:36:13Z,2020-02-13T06:36:13Z
 * ```
 * 
 *  The `triggers` argument cannot be imported.
 * 
 */
@ResourceType(type="time:index/timeRotating:TimeRotating")
public class TimeRotating extends com.pulumi.resources.CustomResource {
    /**
     * Number day of timestamp.
     * 
     */
    @Export(name="day", type=Integer.class, parameters={})
    private Output<Integer> day;

    /**
     * @return Number day of timestamp.
     * 
     */
    public Output<Integer> day() {
        return this.day;
    }
    /**
     * Number hour of timestamp.
     * 
     */
    @Export(name="hour", type=Integer.class, parameters={})
    private Output<Integer> hour;

    /**
     * @return Number hour of timestamp.
     * 
     */
    public Output<Integer> hour() {
        return this.hour;
    }
    /**
     * Number minute of timestamp.
     * 
     */
    @Export(name="minute", type=Integer.class, parameters={})
    private Output<Integer> minute;

    /**
     * @return Number minute of timestamp.
     * 
     */
    public Output<Integer> minute() {
        return this.minute;
    }
    /**
     * Number month of timestamp.
     * 
     */
    @Export(name="month", type=Integer.class, parameters={})
    private Output<Integer> month;

    /**
     * @return Number month of timestamp.
     * 
     */
    public Output<Integer> month() {
        return this.month;
    }
    /**
     * Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    @Export(name="rfc3339", type=String.class, parameters={})
    private Output<String> rfc3339;

    /**
     * @return Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    public Output<String> rfc3339() {
        return this.rfc3339;
    }
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationDays", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> rotationDays;

    /**
     * @return Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<Optional<Integer>> rotationDays() {
        return Codegen.optional(this.rotationDays);
    }
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationHours", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> rotationHours;

    /**
     * @return Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<Optional<Integer>> rotationHours() {
        return Codegen.optional(this.rotationHours);
    }
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationMinutes", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> rotationMinutes;

    /**
     * @return Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<Optional<Integer>> rotationMinutes() {
        return Codegen.optional(this.rotationMinutes);
    }
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationMonths", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> rotationMonths;

    /**
     * @return Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<Optional<Integer>> rotationMonths() {
        return Codegen.optional(this.rotationMonths);
    }
    /**
     * Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationRfc3339", type=String.class, parameters={})
    private Output<String> rotationRfc3339;

    /**
     * @return Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<String> rotationRfc3339() {
        return this.rotationRfc3339;
    }
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    @Export(name="rotationYears", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> rotationYears;

    /**
     * @return Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     * 
     */
    public Output<Optional<Integer>> rotationYears() {
        return Codegen.optional(this.rotationYears);
    }
    /**
     * Number second of timestamp.
     * 
     */
    @Export(name="second", type=Integer.class, parameters={})
    private Output<Integer> second;

    /**
     * @return Number second of timestamp.
     * 
     */
    public Output<Integer> second() {
        return this.second;
    }
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See the main provider documentation for more information.
     * 
     */
    @Export(name="triggers", type=Map.class, parameters={String.class, String.class})
    private Output</* @Nullable */ Map<String,String>> triggers;

    /**
     * @return Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See the main provider documentation for more information.
     * 
     */
    public Output<Optional<Map<String,String>>> triggers() {
        return Codegen.optional(this.triggers);
    }
    /**
     * Number of seconds since epoch time, e.g. `1581489373`.
     * 
     */
    @Export(name="unix", type=Integer.class, parameters={})
    private Output<Integer> unix;

    /**
     * @return Number of seconds since epoch time, e.g. `1581489373`.
     * 
     */
    public Output<Integer> unix() {
        return this.unix;
    }
    /**
     * Number year of timestamp.
     * 
     */
    @Export(name="year", type=Integer.class, parameters={})
    private Output<Integer> year;

    /**
     * @return Number year of timestamp.
     * 
     */
    public Output<Integer> year() {
        return this.year;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public TimeRotating(String name) {
        this(name, TimeRotatingArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public TimeRotating(String name, @Nullable TimeRotatingArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public TimeRotating(String name, @Nullable TimeRotatingArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/timeRotating:TimeRotating", name, args == null ? TimeRotatingArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private TimeRotating(String name, Output<String> id, @Nullable TimeRotatingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/timeRotating:TimeRotating", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static TimeRotating get(String name, Output<String> id, @Nullable TimeRotatingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new TimeRotating(name, id, state, options);
    }
}