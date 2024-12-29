// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumiverse.time;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumiverse.time.SleepArgs;
import com.pulumiverse.time.Utilities;
import com.pulumiverse.time.inputs.SleepState;
import java.lang.String;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * 
 * ### Delay Create Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.null.Resource;
 * import com.pulumi.time.Sleep;
 * import com.pulumi.time.SleepArgs;
 * import com.pulumi.null.ResourceArgs;
 * import com.pulumi.resources.CustomResourceOptions;
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
 *         // This resource will destroy (potentially immediately) after null_resource.next
 *         var previous = new Resource(&#34;previous&#34;);
 * 
 *         var wait30Seconds = new Sleep(&#34;wait30Seconds&#34;, SleepArgs.builder()
 *             .createDuration(&#34;30s&#34;)
 *             .build(), CustomResourceOptions.builder()
 *                 .dependsOn(previous)
 *                 .build());
 * 
 *         // This resource will create (at least) 30 seconds after null_resource.previous
 *         var next = new Resource(&#34;next&#34;, ResourceArgs.Empty, CustomResourceOptions.builder()
 *             .dependsOn(wait30Seconds)
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ### Delay Destroy Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.null.Resource;
 * import com.pulumi.time.Sleep;
 * import com.pulumi.time.SleepArgs;
 * import com.pulumi.null.ResourceArgs;
 * import com.pulumi.resources.CustomResourceOptions;
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
 *         // This resource will destroy (at least) 30 seconds after null_resource.next
 *         var previous = new Resource(&#34;previous&#34;);
 * 
 *         var wait30Seconds = new Sleep(&#34;wait30Seconds&#34;, SleepArgs.builder()
 *             .destroyDuration(&#34;30s&#34;)
 *             .build(), CustomResourceOptions.builder()
 *                 .dependsOn(previous)
 *                 .build());
 * 
 *         // This resource will create (potentially immediately) after null_resource.previous
 *         var next = new Resource(&#34;next&#34;, ResourceArgs.Empty, CustomResourceOptions.builder()
 *             .dependsOn(wait30Seconds)
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ### Triggers Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.aws.ram.ResourceAssociation;
 * import com.pulumi.aws.ram.ResourceAssociationArgs;
 * import com.pulumi.time.Sleep;
 * import com.pulumi.time.SleepArgs;
 * import com.pulumi.aws.rds.SubnetGroup;
 * import com.pulumi.aws.rds.SubnetGroupArgs;
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
 *         var exampleResourceAssociation = new ResourceAssociation(&#34;exampleResourceAssociation&#34;, ResourceAssociationArgs.builder()
 *             .resourceArn(aws_subnet.example().arn())
 *             .resourceShareArn(aws_ram_resource_share.example().arn())
 *             .build());
 * 
 *         // AWS resources shared via Resource Access Manager can take a few seconds to
 *         // propagate across AWS accounts after RAM returns a successful association.
 *         var ramResourcePropagation = new Sleep(&#34;ramResourcePropagation&#34;, SleepArgs.builder()
 *             .createDuration(&#34;60s&#34;)
 *             .triggers(Map.ofEntries(
 *                 Map.entry(&#34;subnet_arn&#34;, exampleResourceAssociation.resourceArn()),
 *                 Map.entry(&#34;subnet_id&#34;, aws_subnet.example().id())
 *             ))
 *             .build());
 * 
 *         var exampleSubnetGroup = new SubnetGroup(&#34;exampleSubnetGroup&#34;, SubnetGroupArgs.builder()
 *             .subnetIds(ramResourcePropagation.triggers().applyValue(triggers -&gt; triggers.subnet_id()))
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`).
 * 
 * e.g. For 30 seconds create duration with no destroy duration:
 * 
 * ```sh
 * $ pulumi import time:index/sleep:Sleep example 30s,
 * ```
 * 
 * e.g. For 30 seconds destroy duration with no create duration:
 * 
 * ```sh
 * $ pulumi import time:index/sleep:Sleep example ,30s
 * ```
 * 
 * The `triggers` argument cannot be imported.
 * 
 */
@ResourceType(type="time:index/sleep:Sleep")
public class Sleep extends com.pulumi.resources.CustomResource {
    /**
     * [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
     * 
     */
    @Export(name="createDuration", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> createDuration;

    /**
     * @return [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
     * 
     */
    public Output<Optional<String>> createDuration() {
        return Codegen.optional(this.createDuration);
    }
    @Export(name="destroyDuration", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> destroyDuration;

    public Output<Optional<String>> destroyDuration() {
        return Codegen.optional(this.destroyDuration);
    }
    /**
     * (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
     * 
     */
    @Export(name="triggers", refs={Map.class,String.class}, tree="[0,1,1]")
    private Output</* @Nullable */ Map<String,String>> triggers;

    /**
     * @return (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
     * 
     */
    public Output<Optional<Map<String,String>>> triggers() {
        return Codegen.optional(this.triggers);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Sleep(String name) {
        this(name, SleepArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Sleep(String name, @Nullable SleepArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Sleep(String name, @Nullable SleepArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/sleep:Sleep", name, args == null ? SleepArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Sleep(String name, Output<String> id, @Nullable SleepState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("time:index/sleep:Sleep", name, state, makeResourceOptions(options, id));
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
    public static Sleep get(String name, Output<String> id, @Nullable SleepState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Sleep(name, id, state, options);
    }
}