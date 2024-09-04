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
    /// 
    /// ### Delay Create Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Null = Pulumi.Null;
    /// using Time = Pulumiverse.Time;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // This resource will destroy (potentially immediately) after null_resource.next
    ///     var previous = new Null.Resource("previous");
    /// 
    ///     var wait30Seconds = new Time.Sleep("wait30Seconds", new()
    ///     {
    ///         CreateDuration = "30s",
    ///     }, new CustomResourceOptions
    ///     {
    ///         DependsOn =
    ///         {
    ///             previous,
    ///         },
    ///     });
    /// 
    ///     // This resource will create (at least) 30 seconds after null_resource.previous
    ///     var next = new Null.Resource("next", new()
    ///     {
    ///     }, new CustomResourceOptions
    ///     {
    ///         DependsOn =
    ///         {
    ///             wait30Seconds,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Delay Destroy Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Null = Pulumi.Null;
    /// using Time = Pulumiverse.Time;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // This resource will destroy (at least) 30 seconds after null_resource.next
    ///     var previous = new Null.Resource("previous");
    /// 
    ///     var wait30Seconds = new Time.Sleep("wait30Seconds", new()
    ///     {
    ///         DestroyDuration = "30s",
    ///     }, new CustomResourceOptions
    ///     {
    ///         DependsOn =
    ///         {
    ///             previous,
    ///         },
    ///     });
    /// 
    ///     // This resource will create (potentially immediately) after null_resource.previous
    ///     var next = new Null.Resource("next", new()
    ///     {
    ///     }, new CustomResourceOptions
    ///     {
    ///         DependsOn =
    ///         {
    ///             wait30Seconds,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Triggers Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// using Time = Pulumiverse.Time;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleResourceAssociation = new Aws.Ram.ResourceAssociation("exampleResourceAssociation", new()
    ///     {
    ///         ResourceArn = aws_subnet.Example.Arn,
    ///         ResourceShareArn = aws_ram_resource_share.Example.Arn,
    ///     });
    /// 
    ///     // AWS resources shared via Resource Access Manager can take a few seconds to
    ///     // propagate across AWS accounts after RAM returns a successful association.
    ///     var ramResourcePropagation = new Time.Sleep("ramResourcePropagation", new()
    ///     {
    ///         CreateDuration = "60s",
    ///         Triggers = 
    ///         {
    ///             { "subnet_arn", exampleResourceAssociation.ResourceArn },
    ///             { "subnet_id", aws_subnet.Example.Id },
    ///         },
    ///     });
    /// 
    ///     var exampleSubnetGroup = new Aws.Rds.SubnetGroup("exampleSubnetGroup", new()
    ///     {
    ///         SubnetIds = new[]
    ///         {
    ///             ramResourcePropagation.Triggers.Apply(triggers =&gt; triggers?.Subnet_id),
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`).
    /// 
    /// e.g. For 30 seconds create duration with no destroy duration:
    /// 
    /// ```sh
    /// $ pulumi import time:index/sleep:Sleep example 30s,
    /// ```
    /// 
    /// e.g. For 30 seconds destroy duration with no create duration:
    /// 
    /// ```sh
    /// $ pulumi import time:index/sleep:Sleep example ,30s
    /// ```
    /// 
    /// The `triggers` argument cannot be imported.
    /// </summary>
    [TimeResourceType("time:index/sleep:Sleep")]
    public partial class Sleep : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        /// </summary>
        [Output("createDuration")]
        public Output<string?> CreateDuration { get; private set; } = null!;

        [Output("destroyDuration")]
        public Output<string?> DestroyDuration { get; private set; } = null!;

        /// <summary>
        /// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        /// </summary>
        [Output("triggers")]
        public Output<ImmutableDictionary<string, string>?> Triggers { get; private set; } = null!;


        /// <summary>
        /// Create a Sleep resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Sleep(string name, SleepArgs? args = null, CustomResourceOptions? options = null)
            : base("time:index/sleep:Sleep", name, args ?? new SleepArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Sleep(string name, Input<string> id, SleepState? state = null, CustomResourceOptions? options = null)
            : base("time:index/sleep:Sleep", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Sleep resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Sleep Get(string name, Input<string> id, SleepState? state = null, CustomResourceOptions? options = null)
        {
            return new Sleep(name, id, state, options);
        }
    }

    public sealed class SleepArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        /// </summary>
        [Input("createDuration")]
        public Input<string>? CreateDuration { get; set; }

        [Input("destroyDuration")]
        public Input<string>? DestroyDuration { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        public SleepArgs()
        {
        }
        public static new SleepArgs Empty => new SleepArgs();
    }

    public sealed class SleepState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        /// </summary>
        [Input("createDuration")]
        public Input<string>? CreateDuration { get; set; }

        [Input("destroyDuration")]
        public Input<string>? DestroyDuration { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        public SleepState()
        {
        }
        public static new SleepState Empty => new SleepState();
    }
}
