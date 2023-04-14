// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumiverse.time;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumiverse.time.RotatingArgs;
import com.pulumiverse.time.Utilities;
import com.pulumiverse.time.inputs.RotatingState;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * ### Basic Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.time.Rotating;
 * import com.pulumi.time.RotatingArgs;
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
 *         var example = new Rotating(&#34;example&#34;, RotatingArgs.builder()        
 *             .rotationDays(30)
 *             .build());
 * 
 *     }
 * }
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
 * 
 */
@ResourceType(type="time:index/rotating:Rotating")
public class Rotating extends com.pulumi.resources.CustomResource {
    /**
     * Number day of timestamp.
     * 
     */
    @Export(name="day", refs={Integer.class}, tree="[0]")
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
    @Export(name="hour", refs={Integer.class}, tree="[0]")
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
    @Export(name="minute", refs={Integer.class}, tree="[0]")
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
    @Export(name="month", refs={Integer.class}, tree="[0]")
    private Output<Integer> month;

    /**
     * @return Number month of timestamp.
     * 
     */
    public Output<Integer> month() {
        return this.month;
    }
    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    @Export(name="rfc3339", refs={String.class}, tree="[0]")
    private Output<String> rfc3339;

    /**
     * @return Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    public Output<String> rfc3339() {
        return this.rfc3339;
    }
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationDays", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> rotationDays;

    /**
     * @return Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<Optional<Integer>> rotationDays() {
        return Codegen.optional(this.rotationDays);
    }
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationHours", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> rotationHours;

    /**
     * @return Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<Optional<Integer>> rotationHours() {
        return Codegen.optional(this.rotationHours);
    }
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationMinutes", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> rotationMinutes;

    /**
     * @return Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<Optional<Integer>> rotationMinutes() {
        return Codegen.optional(this.rotationMinutes);
    }
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationMonths", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> rotationMonths;

    /**
     * @return Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<Optional<Integer>> rotationMonths() {
        return Codegen.optional(this.rotationMonths);
    }
    /**
     * Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationRfc3339", refs={String.class}, tree="[0]")
    private Output<String> rotationRfc3339;

    /**
     * @return Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<String> rotationRfc3339() {
        return this.rotationRfc3339;
    }
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Export(name="rotationYears", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> rotationYears;

    /**
     * @return Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Output<Optional<Integer>> rotationYears() {
        return Codegen.optional(this.rotationYears);
    }
    /**
     * Number second of timestamp.
     * 
     */
    @Export(name="second", refs={Integer.class}, tree="[0]")
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
    @Export(name="triggers", refs={Map.class,String.class}, tree="[0,1,1]")
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
    @Export(name="unix", refs={Integer.class}, tree="[0]")
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
    @Export(name="year", refs={Integer.class}, tree="[0]")
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
    public Rotating(String name) {
        this(name, RotatingArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Rotating(String name, @Nullable RotatingArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Rotating(String name, @Nullable RotatingArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/rotating:Rotating", name, args == null ? RotatingArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Rotating(String name, Output<String> id, @Nullable RotatingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/rotating:Rotating", name, state, makeResourceOptions(options, id));
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
    public static Rotating get(String name, Output<String> id, @Nullable RotatingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Rotating(name, id, state, options);
    }
}
