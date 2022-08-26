// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumiverse.time;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RotatingArgs extends com.pulumi.resources.ResourceArgs {

    public static final RotatingArgs Empty = new RotatingArgs();

    /**
     * Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
     * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    @Import(name="rfc3339")
    private @Nullable Output<String> rfc3339;

    /**
     * @return Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
     * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     * 
     */
    public Optional<Output<String>> rfc3339() {
        return Optional.ofNullable(this.rfc3339);
    }

    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationDays")
    private @Nullable Output<Integer> rotationDays;

    /**
     * @return Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<Integer>> rotationDays() {
        return Optional.ofNullable(this.rotationDays);
    }

    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationHours")
    private @Nullable Output<Integer> rotationHours;

    /**
     * @return Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<Integer>> rotationHours() {
        return Optional.ofNullable(this.rotationHours);
    }

    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationMinutes")
    private @Nullable Output<Integer> rotationMinutes;

    /**
     * @return Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<Integer>> rotationMinutes() {
        return Optional.ofNullable(this.rotationMinutes);
    }

    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationMonths")
    private @Nullable Output<Integer> rotationMonths;

    /**
     * @return Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<Integer>> rotationMonths() {
        return Optional.ofNullable(this.rotationMonths);
    }

    /**
     * Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
     * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
     * least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationRfc3339")
    private @Nullable Output<String> rotationRfc3339;

    /**
     * @return Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
     * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
     * least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<String>> rotationRfc3339() {
        return Optional.ofNullable(this.rotationRfc3339);
    }

    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    @Import(name="rotationYears")
    private @Nullable Output<Integer> rotationYears;

    /**
     * @return Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
     * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
     * 
     */
    public Optional<Output<Integer>> rotationYears() {
        return Optional.ofNullable(this.rotationYears);
    }

    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
     * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
     * more information.
     * 
     */
    @Import(name="triggers")
    private @Nullable Output<Map<String,String>> triggers;

    /**
     * @return Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
     * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
     * more information.
     * 
     */
    public Optional<Output<Map<String,String>>> triggers() {
        return Optional.ofNullable(this.triggers);
    }

    private RotatingArgs() {}

    private RotatingArgs(RotatingArgs $) {
        this.rfc3339 = $.rfc3339;
        this.rotationDays = $.rotationDays;
        this.rotationHours = $.rotationHours;
        this.rotationMinutes = $.rotationMinutes;
        this.rotationMonths = $.rotationMonths;
        this.rotationRfc3339 = $.rotationRfc3339;
        this.rotationYears = $.rotationYears;
        this.triggers = $.triggers;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RotatingArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RotatingArgs $;

        public Builder() {
            $ = new RotatingArgs();
        }

        public Builder(RotatingArgs defaults) {
            $ = new RotatingArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param rfc3339 Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
         * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
         * 
         * @return builder
         * 
         */
        public Builder rfc3339(@Nullable Output<String> rfc3339) {
            $.rfc3339 = rfc3339;
            return this;
        }

        /**
         * @param rfc3339 Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
         * string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
         * 
         * @return builder
         * 
         */
        public Builder rfc3339(String rfc3339) {
            return rfc3339(Output.of(rfc3339));
        }

        /**
         * @param rotationDays Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationDays(@Nullable Output<Integer> rotationDays) {
            $.rotationDays = rotationDays;
            return this;
        }

        /**
         * @param rotationDays Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationDays(Integer rotationDays) {
            return rotationDays(Output.of(rotationDays));
        }

        /**
         * @param rotationHours Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationHours(@Nullable Output<Integer> rotationHours) {
            $.rotationHours = rotationHours;
            return this;
        }

        /**
         * @param rotationHours Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationHours(Integer rotationHours) {
            return rotationHours(Output.of(rotationHours));
        }

        /**
         * @param rotationMinutes Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationMinutes(@Nullable Output<Integer> rotationMinutes) {
            $.rotationMinutes = rotationMinutes;
            return this;
        }

        /**
         * @param rotationMinutes Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationMinutes(Integer rotationMinutes) {
            return rotationMinutes(Output.of(rotationMinutes));
        }

        /**
         * @param rotationMonths Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationMonths(@Nullable Output<Integer> rotationMonths) {
            $.rotationMonths = rotationMonths;
            return this;
        }

        /**
         * @param rotationMonths Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationMonths(Integer rotationMonths) {
            return rotationMonths(Output.of(rotationMonths));
        }

        /**
         * @param rotationRfc3339 Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
         * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
         * least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationRfc3339(@Nullable Output<String> rotationRfc3339) {
            $.rotationRfc3339 = rotationRfc3339;
            return this;
        }

        /**
         * @param rotationRfc3339 Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
         * the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
         * least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationRfc3339(String rotationRfc3339) {
            return rotationRfc3339(Output.of(rotationRfc3339));
        }

        /**
         * @param rotationYears Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationYears(@Nullable Output<Integer> rotationYears) {
            $.rotationYears = rotationYears;
            return this;
        }

        /**
         * @param rotationYears Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
         * rotation timestamp, the resource will trigger recreation. At least one of the &#39;rotation_&#39; arguments must be configured.
         * 
         * @return builder
         * 
         */
        public Builder rotationYears(Integer rotationYears) {
            return rotationYears(Output.of(rotationYears));
        }

        /**
         * @param triggers Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
         * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
         * more information.
         * 
         * @return builder
         * 
         */
        public Builder triggers(@Nullable Output<Map<String,String>> triggers) {
            $.triggers = triggers;
            return this;
        }

        /**
         * @param triggers Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
         * recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
         * more information.
         * 
         * @return builder
         * 
         */
        public Builder triggers(Map<String,String> triggers) {
            return triggers(Output.of(triggers));
        }

        public RotatingArgs build() {
            return $;
        }
    }

}
