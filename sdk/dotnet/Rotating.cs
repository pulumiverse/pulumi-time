// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Time
{
    /// <summary>
    /// ## Example Usage
    /// ### Basic Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Time = Pulumiverse.Time;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Time.Rotating("example", new Time.RotatingArgs
    ///         {
    ///             RotationDays = 30,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// This resource can be imported using the base UTC RFC3339 value and rotation years, months, days, hours, and minutes, separated by commas (`,`), e.g. for 30 days
    /// 
    /// ```sh
    ///  $ pulumi import time:index/rotating:Rotating example 2020-02-12T06:36:13Z,0,0,30,0,0
    /// ```
    /// 
    ///  Otherwise, to import with the rotation RFC3339 value, the base UTC RFC3339 value and rotation UTC RFC3339 value, separated by commas (`,`), e.g.
    /// 
    /// ```sh
    ///  $ pulumi import time:index/rotating:Rotating example 2020-02-12T06:36:13Z,2020-02-13T06:36:13Z
    /// ```
    /// 
    ///  The `triggers` argument cannot be imported.
    /// </summary>
    [TimeResourceType("time:index/rotating:Rotating")]
    public partial class Rotating : Pulumi.CustomResource
    {
        /// <summary>
        /// Number day of timestamp.
        /// </summary>
        [Output("day")]
        public Output<int> Day { get; private set; } = null!;

        /// <summary>
        /// Number hour of timestamp.
        /// </summary>
        [Output("hour")]
        public Output<int> Hour { get; private set; } = null!;

        /// <summary>
        /// Number minute of timestamp.
        /// </summary>
        [Output("minute")]
        public Output<int> Minute { get; private set; } = null!;

        /// <summary>
        /// Number month of timestamp.
        /// </summary>
        [Output("month")]
        public Output<int> Month { get; private set; } = null!;

        /// <summary>
        /// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
        /// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Output("rfc3339")]
        public Output<string> Rfc3339 { get; private set; } = null!;

        /// <summary>
        /// Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationDays")]
        public Output<int?> RotationDays { get; private set; } = null!;

        /// <summary>
        /// Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationHours")]
        public Output<int?> RotationHours { get; private set; } = null!;

        /// <summary>
        /// Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationMinutes")]
        public Output<int?> RotationMinutes { get; private set; } = null!;

        /// <summary>
        /// Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationMonths")]
        public Output<int?> RotationMonths { get; private set; } = null!;

        /// <summary>
        /// Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
        /// the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
        /// least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationRfc3339")]
        public Output<string> RotationRfc3339 { get; private set; } = null!;

        /// <summary>
        /// Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Output("rotationYears")]
        public Output<int?> RotationYears { get; private set; } = null!;

        /// <summary>
        /// Number second of timestamp.
        /// </summary>
        [Output("second")]
        public Output<int> Second { get; private set; } = null!;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
        /// recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
        /// more information.
        /// </summary>
        [Output("triggers")]
        public Output<ImmutableDictionary<string, string>?> Triggers { get; private set; } = null!;

        /// <summary>
        /// Number of seconds since epoch time, e.g. `1581489373`.
        /// </summary>
        [Output("unix")]
        public Output<int> Unix { get; private set; } = null!;

        /// <summary>
        /// Number year of timestamp.
        /// </summary>
        [Output("year")]
        public Output<int> Year { get; private set; } = null!;


        /// <summary>
        /// Create a Rotating resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rotating(string name, RotatingArgs? args = null, CustomResourceOptions? options = null)
            : base("time:index/rotating:Rotating", name, args ?? new RotatingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rotating(string name, Input<string> id, RotatingState? state = null, CustomResourceOptions? options = null)
            : base("time:index/rotating:Rotating", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse/pulumi-time",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Rotating resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Rotating Get(string name, Input<string> id, RotatingState? state = null, CustomResourceOptions? options = null)
        {
            return new Rotating(name, id, state, options);
        }
    }

    public sealed class RotatingArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
        /// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Input("rfc3339")]
        public Input<string>? Rfc3339 { get; set; }

        /// <summary>
        /// Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationDays")]
        public Input<int>? RotationDays { get; set; }

        /// <summary>
        /// Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationHours")]
        public Input<int>? RotationHours { get; set; }

        /// <summary>
        /// Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationMinutes")]
        public Input<int>? RotationMinutes { get; set; }

        /// <summary>
        /// Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationMonths")]
        public Input<int>? RotationMonths { get; set; }

        /// <summary>
        /// Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
        /// the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
        /// least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationRfc3339")]
        public Input<string>? RotationRfc3339 { get; set; }

        /// <summary>
        /// Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationYears")]
        public Input<int>? RotationYears { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
        /// recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
        /// more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        public RotatingArgs()
        {
        }
    }

    public sealed class RotatingState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Number day of timestamp.
        /// </summary>
        [Input("day")]
        public Input<int>? Day { get; set; }

        /// <summary>
        /// Number hour of timestamp.
        /// </summary>
        [Input("hour")]
        public Input<int>? Hour { get; set; }

        /// <summary>
        /// Number minute of timestamp.
        /// </summary>
        [Input("minute")]
        public Input<int>? Minute { get; set; }

        /// <summary>
        /// Number month of timestamp.
        /// </summary>
        [Input("month")]
        public Input<int>? Month { get; set; }

        /// <summary>
        /// Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time
        /// string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Input("rfc3339")]
        public Input<string>? Rfc3339 { get; set; }

        /// <summary>
        /// Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationDays")]
        public Input<int>? RotationDays { get; set; }

        /// <summary>
        /// Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationHours")]
        public Input<int>? RotationHours { get; set; }

        /// <summary>
        /// Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationMinutes")]
        public Input<int>? RotationMinutes { get; set; }

        /// <summary>
        /// Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationMonths")]
        public Input<int>? RotationMonths { get; set; }

        /// <summary>
        /// Configure the rotation timestamp with an [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format of
        /// the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At
        /// least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationRfc3339")]
        public Input<string>? RotationRfc3339 { get; set; }

        /// <summary>
        /// Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the
        /// rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.
        /// </summary>
        [Input("rotationYears")]
        public Input<int>? RotationYears { get; set; }

        /// <summary>
        /// Number second of timestamp.
        /// </summary>
        [Input("second")]
        public Input<int>? Second { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions
        /// recreate the resource in addition to other rotation arguments. See [the main provider documentation](../index.md) for
        /// more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        /// <summary>
        /// Number of seconds since epoch time, e.g. `1581489373`.
        /// </summary>
        [Input("unix")]
        public Input<int>? Unix { get; set; }

        /// <summary>
        /// Number year of timestamp.
        /// </summary>
        [Input("year")]
        public Input<int>? Year { get; set; }

        public RotatingState()
        {
        }
    }
}