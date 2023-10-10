# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SleepArgs', 'Sleep']

@pulumi.input_type
class SleepArgs:
    def __init__(__self__, *,
                 create_duration: Optional[pulumi.Input[str]] = None,
                 destroy_duration: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Sleep resource.
        :param pulumi.Input[str] create_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        :param pulumi.Input[str] destroy_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
               or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
               successfully applied into the Terraform state before destroying this resource to take effect.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        if create_duration is not None:
            pulumi.set(__self__, "create_duration", create_duration)
        if destroy_duration is not None:
            pulumi.set(__self__, "destroy_duration", destroy_duration)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)

    @property
    @pulumi.getter(name="createDuration")
    def create_duration(self) -> Optional[pulumi.Input[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        """
        return pulumi.get(self, "create_duration")

    @create_duration.setter
    def create_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_duration", value)

    @property
    @pulumi.getter(name="destroyDuration")
    def destroy_duration(self) -> Optional[pulumi.Input[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
        or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
        successfully applied into the Terraform state before destroying this resource to take effect.
        """
        return pulumi.get(self, "destroy_duration")

    @destroy_duration.setter
    def destroy_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destroy_duration", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)


@pulumi.input_type
class _SleepState:
    def __init__(__self__, *,
                 create_duration: Optional[pulumi.Input[str]] = None,
                 destroy_duration: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Sleep resources.
        :param pulumi.Input[str] create_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        :param pulumi.Input[str] destroy_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
               or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
               successfully applied into the Terraform state before destroying this resource to take effect.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        if create_duration is not None:
            pulumi.set(__self__, "create_duration", create_duration)
        if destroy_duration is not None:
            pulumi.set(__self__, "destroy_duration", destroy_duration)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)

    @property
    @pulumi.getter(name="createDuration")
    def create_duration(self) -> Optional[pulumi.Input[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        """
        return pulumi.get(self, "create_duration")

    @create_duration.setter
    def create_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_duration", value)

    @property
    @pulumi.getter(name="destroyDuration")
    def destroy_duration(self) -> Optional[pulumi.Input[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
        or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
        successfully applied into the Terraform state before destroying this resource to take effect.
        """
        return pulumi.get(self, "destroy_duration")

    @destroy_duration.setter
    def destroy_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destroy_duration", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)


class Sleep(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_duration: Optional[pulumi.Input[str]] = None,
                 destroy_duration: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Delay Create Usage

        ```python
        import pulumi
        import pulumi_null as null
        import pulumiverse_time as time

        # This resource will destroy (potentially immediately) after null_resource.next
        previous = null.Resource("previous")
        wait30_seconds = time.Sleep("wait30Seconds", create_duration="30s",
        opts=pulumi.ResourceOptions(depends_on=[previous]))
        # This resource will create (at least) 30 seconds after null_resource.previous
        next = null.Resource("next", opts=pulumi.ResourceOptions(depends_on=[wait30_seconds]))
        ```
        ### Delay Destroy Usage

        ```python
        import pulumi
        import pulumi_null as null
        import pulumiverse_time as time

        # This resource will destroy (at least) 30 seconds after null_resource.next
        previous = null.Resource("previous")
        wait30_seconds = time.Sleep("wait30Seconds", destroy_duration="30s",
        opts=pulumi.ResourceOptions(depends_on=[previous]))
        # This resource will create (potentially immediately) after null_resource.previous
        next = null.Resource("next", opts=pulumi.ResourceOptions(depends_on=[wait30_seconds]))
        ```
        ### Triggers Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumiverse_time as time

        example_resource_association = aws.ram.ResourceAssociation("exampleResourceAssociation",
            resource_arn=aws_subnet["example"]["arn"],
            resource_share_arn=aws_ram_resource_share["example"]["arn"])
        # AWS resources shared via Resource Access Manager can take a few seconds to
        # propagate across AWS accounts after RAM returns a successful association.
        ram_resource_propagation = time.Sleep("ramResourcePropagation",
            create_duration="60s",
            triggers={
                "subnet_arn": example_resource_association.resource_arn,
                "subnet_id": aws_subnet["example"]["id"],
            })
        example_subnet_group = aws.rds.SubnetGroup("exampleSubnetGroup", subnet_ids=[ram_resource_propagation.triggers["subnet_id"]])
        ```

        ## Import

        This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`). e.g. For 30 seconds create duration with no destroy duration

        ```sh
         $ pulumi import time:index/sleep:Sleep example 30s,
        ```

         e.g. For 30 seconds destroy duration with no create duration

        ```sh
         $ pulumi import time:index/sleep:Sleep example ,30s
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        :param pulumi.Input[str] destroy_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
               or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
               successfully applied into the Terraform state before destroying this resource to take effect.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SleepArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Delay Create Usage

        ```python
        import pulumi
        import pulumi_null as null
        import pulumiverse_time as time

        # This resource will destroy (potentially immediately) after null_resource.next
        previous = null.Resource("previous")
        wait30_seconds = time.Sleep("wait30Seconds", create_duration="30s",
        opts=pulumi.ResourceOptions(depends_on=[previous]))
        # This resource will create (at least) 30 seconds after null_resource.previous
        next = null.Resource("next", opts=pulumi.ResourceOptions(depends_on=[wait30_seconds]))
        ```
        ### Delay Destroy Usage

        ```python
        import pulumi
        import pulumi_null as null
        import pulumiverse_time as time

        # This resource will destroy (at least) 30 seconds after null_resource.next
        previous = null.Resource("previous")
        wait30_seconds = time.Sleep("wait30Seconds", destroy_duration="30s",
        opts=pulumi.ResourceOptions(depends_on=[previous]))
        # This resource will create (potentially immediately) after null_resource.previous
        next = null.Resource("next", opts=pulumi.ResourceOptions(depends_on=[wait30_seconds]))
        ```
        ### Triggers Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumiverse_time as time

        example_resource_association = aws.ram.ResourceAssociation("exampleResourceAssociation",
            resource_arn=aws_subnet["example"]["arn"],
            resource_share_arn=aws_ram_resource_share["example"]["arn"])
        # AWS resources shared via Resource Access Manager can take a few seconds to
        # propagate across AWS accounts after RAM returns a successful association.
        ram_resource_propagation = time.Sleep("ramResourcePropagation",
            create_duration="60s",
            triggers={
                "subnet_arn": example_resource_association.resource_arn,
                "subnet_id": aws_subnet["example"]["id"],
            })
        example_subnet_group = aws.rds.SubnetGroup("exampleSubnetGroup", subnet_ids=[ram_resource_propagation.triggers["subnet_id"]])
        ```

        ## Import

        This resource can be imported with the `create_duration` and `destroy_duration`, separated by a comma (`,`). e.g. For 30 seconds create duration with no destroy duration

        ```sh
         $ pulumi import time:index/sleep:Sleep example 30s,
        ```

         e.g. For 30 seconds destroy duration with no create duration

        ```sh
         $ pulumi import time:index/sleep:Sleep example ,30s
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param SleepArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SleepArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_duration: Optional[pulumi.Input[str]] = None,
                 destroy_duration: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SleepArgs.__new__(SleepArgs)

            __props__.__dict__["create_duration"] = create_duration
            __props__.__dict__["destroy_duration"] = destroy_duration
            __props__.__dict__["triggers"] = triggers
        super(Sleep, __self__).__init__(
            'time:index/sleep:Sleep',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_duration: Optional[pulumi.Input[str]] = None,
            destroy_duration: Optional[pulumi.Input[str]] = None,
            triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Sleep':
        """
        Get an existing Sleep resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        :param pulumi.Input[str] destroy_duration: [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
               or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
               successfully applied into the Terraform state before destroying this resource to take effect.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SleepState.__new__(_SleepState)

        __props__.__dict__["create_duration"] = create_duration
        __props__.__dict__["destroy_duration"] = destroy_duration
        __props__.__dict__["triggers"] = triggers
        return Sleep(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createDuration")
    def create_duration(self) -> pulumi.Output[Optional[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource creation. For example, `30s` for 30 seconds or `5m` for 5 minutes. Updating this value by itself will not trigger a delay.
        """
        return pulumi.get(self, "create_duration")

    @property
    @pulumi.getter(name="destroyDuration")
    def destroy_duration(self) -> pulumi.Output[Optional[str]]:
        """
        [Time duration](https://golang.org/pkg/time/#ParseDuration) to delay resource destroy. For example, `30s` for 30 seconds
        or `5m` for 5 minutes. Updating this value by itself will not trigger a delay. This value or any updates to it must be
        successfully applied into the Terraform state before destroying this resource to take effect.
        """
        return pulumi.get(self, "destroy_duration")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        (Optional) Arbitrary map of values that, when changed, will run any creation or destroy delays again. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

