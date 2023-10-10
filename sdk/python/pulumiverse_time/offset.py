# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OffsetArgs', 'Offset']

@pulumi.input_type
class OffsetArgs:
    def __init__(__self__, *,
                 base_rfc3339: Optional[pulumi.Input[str]] = None,
                 offset_days: Optional[pulumi.Input[int]] = None,
                 offset_hours: Optional[pulumi.Input[int]] = None,
                 offset_minutes: Optional[pulumi.Input[int]] = None,
                 offset_months: Optional[pulumi.Input[int]] = None,
                 offset_seconds: Optional[pulumi.Input[int]] = None,
                 offset_years: Optional[pulumi.Input[int]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Offset resource.
        :param pulumi.Input[str] base_rfc3339: Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        if base_rfc3339 is not None:
            pulumi.set(__self__, "base_rfc3339", base_rfc3339)
        if offset_days is not None:
            pulumi.set(__self__, "offset_days", offset_days)
        if offset_hours is not None:
            pulumi.set(__self__, "offset_hours", offset_hours)
        if offset_minutes is not None:
            pulumi.set(__self__, "offset_minutes", offset_minutes)
        if offset_months is not None:
            pulumi.set(__self__, "offset_months", offset_months)
        if offset_seconds is not None:
            pulumi.set(__self__, "offset_seconds", offset_seconds)
        if offset_years is not None:
            pulumi.set(__self__, "offset_years", offset_years)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)

    @property
    @pulumi.getter(name="baseRfc3339")
    def base_rfc3339(self) -> Optional[pulumi.Input[str]]:
        """
        Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "base_rfc3339")

    @base_rfc3339.setter
    def base_rfc3339(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_rfc3339", value)

    @property
    @pulumi.getter(name="offsetDays")
    def offset_days(self) -> Optional[pulumi.Input[int]]:
        """
        Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_days")

    @offset_days.setter
    def offset_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_days", value)

    @property
    @pulumi.getter(name="offsetHours")
    def offset_hours(self) -> Optional[pulumi.Input[int]]:
        """
        Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_hours")

    @offset_hours.setter
    def offset_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_hours", value)

    @property
    @pulumi.getter(name="offsetMinutes")
    def offset_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_minutes")

    @offset_minutes.setter
    def offset_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_minutes", value)

    @property
    @pulumi.getter(name="offsetMonths")
    def offset_months(self) -> Optional[pulumi.Input[int]]:
        """
        Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_months")

    @offset_months.setter
    def offset_months(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_months", value)

    @property
    @pulumi.getter(name="offsetSeconds")
    def offset_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_seconds")

    @offset_seconds.setter
    def offset_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_seconds", value)

    @property
    @pulumi.getter(name="offsetYears")
    def offset_years(self) -> Optional[pulumi.Input[int]]:
        """
        Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_years")

    @offset_years.setter
    def offset_years(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_years", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)


@pulumi.input_type
class _OffsetState:
    def __init__(__self__, *,
                 base_rfc3339: Optional[pulumi.Input[str]] = None,
                 day: Optional[pulumi.Input[int]] = None,
                 hour: Optional[pulumi.Input[int]] = None,
                 minute: Optional[pulumi.Input[int]] = None,
                 month: Optional[pulumi.Input[int]] = None,
                 offset_days: Optional[pulumi.Input[int]] = None,
                 offset_hours: Optional[pulumi.Input[int]] = None,
                 offset_minutes: Optional[pulumi.Input[int]] = None,
                 offset_months: Optional[pulumi.Input[int]] = None,
                 offset_seconds: Optional[pulumi.Input[int]] = None,
                 offset_years: Optional[pulumi.Input[int]] = None,
                 rfc3339: Optional[pulumi.Input[str]] = None,
                 second: Optional[pulumi.Input[int]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unix: Optional[pulumi.Input[int]] = None,
                 year: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Offset resources.
        :param pulumi.Input[str] base_rfc3339: Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] day: Number day of offset timestamp.
        :param pulumi.Input[int] hour: Number hour of offset timestamp.
        :param pulumi.Input[int] minute: Number minute of offset timestamp.
        :param pulumi.Input[int] month: Number month of offset timestamp.
        :param pulumi.Input[int] offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[str] rfc3339: RFC3339 format of the offset timestamp, e.g. `2020-02-12T06:36:13Z`.
        :param pulumi.Input[int] second: Number second of offset timestamp.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        :param pulumi.Input[int] unix: Number of seconds since epoch time, e.g. `1581489373`.
        :param pulumi.Input[int] year: Number year of offset timestamp.
        """
        if base_rfc3339 is not None:
            pulumi.set(__self__, "base_rfc3339", base_rfc3339)
        if day is not None:
            pulumi.set(__self__, "day", day)
        if hour is not None:
            pulumi.set(__self__, "hour", hour)
        if minute is not None:
            pulumi.set(__self__, "minute", minute)
        if month is not None:
            pulumi.set(__self__, "month", month)
        if offset_days is not None:
            pulumi.set(__self__, "offset_days", offset_days)
        if offset_hours is not None:
            pulumi.set(__self__, "offset_hours", offset_hours)
        if offset_minutes is not None:
            pulumi.set(__self__, "offset_minutes", offset_minutes)
        if offset_months is not None:
            pulumi.set(__self__, "offset_months", offset_months)
        if offset_seconds is not None:
            pulumi.set(__self__, "offset_seconds", offset_seconds)
        if offset_years is not None:
            pulumi.set(__self__, "offset_years", offset_years)
        if rfc3339 is not None:
            pulumi.set(__self__, "rfc3339", rfc3339)
        if second is not None:
            pulumi.set(__self__, "second", second)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)
        if unix is not None:
            pulumi.set(__self__, "unix", unix)
        if year is not None:
            pulumi.set(__self__, "year", year)

    @property
    @pulumi.getter(name="baseRfc3339")
    def base_rfc3339(self) -> Optional[pulumi.Input[str]]:
        """
        Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "base_rfc3339")

    @base_rfc3339.setter
    def base_rfc3339(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_rfc3339", value)

    @property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[int]]:
        """
        Number day of offset timestamp.
        """
        return pulumi.get(self, "day")

    @day.setter
    def day(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "day", value)

    @property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[int]]:
        """
        Number hour of offset timestamp.
        """
        return pulumi.get(self, "hour")

    @hour.setter
    def hour(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hour", value)

    @property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[int]]:
        """
        Number minute of offset timestamp.
        """
        return pulumi.get(self, "minute")

    @minute.setter
    def minute(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minute", value)

    @property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[int]]:
        """
        Number month of offset timestamp.
        """
        return pulumi.get(self, "month")

    @month.setter
    def month(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "month", value)

    @property
    @pulumi.getter(name="offsetDays")
    def offset_days(self) -> Optional[pulumi.Input[int]]:
        """
        Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_days")

    @offset_days.setter
    def offset_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_days", value)

    @property
    @pulumi.getter(name="offsetHours")
    def offset_hours(self) -> Optional[pulumi.Input[int]]:
        """
        Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_hours")

    @offset_hours.setter
    def offset_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_hours", value)

    @property
    @pulumi.getter(name="offsetMinutes")
    def offset_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_minutes")

    @offset_minutes.setter
    def offset_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_minutes", value)

    @property
    @pulumi.getter(name="offsetMonths")
    def offset_months(self) -> Optional[pulumi.Input[int]]:
        """
        Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_months")

    @offset_months.setter
    def offset_months(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_months", value)

    @property
    @pulumi.getter(name="offsetSeconds")
    def offset_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_seconds")

    @offset_seconds.setter
    def offset_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_seconds", value)

    @property
    @pulumi.getter(name="offsetYears")
    def offset_years(self) -> Optional[pulumi.Input[int]]:
        """
        Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_years")

    @offset_years.setter
    def offset_years(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "offset_years", value)

    @property
    @pulumi.getter
    def rfc3339(self) -> Optional[pulumi.Input[str]]:
        """
        RFC3339 format of the offset timestamp, e.g. `2020-02-12T06:36:13Z`.
        """
        return pulumi.get(self, "rfc3339")

    @rfc3339.setter
    def rfc3339(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rfc3339", value)

    @property
    @pulumi.getter
    def second(self) -> Optional[pulumi.Input[int]]:
        """
        Number second of offset timestamp.
        """
        return pulumi.get(self, "second")

    @second.setter
    def second(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "second", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)

    @property
    @pulumi.getter
    def unix(self) -> Optional[pulumi.Input[int]]:
        """
        Number of seconds since epoch time, e.g. `1581489373`.
        """
        return pulumi.get(self, "unix")

    @unix.setter
    def unix(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "unix", value)

    @property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[int]]:
        """
        Number year of offset timestamp.
        """
        return pulumi.get(self, "year")

    @year.setter
    def year(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "year", value)


class Offset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_rfc3339: Optional[pulumi.Input[str]] = None,
                 offset_days: Optional[pulumi.Input[int]] = None,
                 offset_hours: Optional[pulumi.Input[int]] = None,
                 offset_minutes: Optional[pulumi.Input[int]] = None,
                 offset_months: Optional[pulumi.Input[int]] = None,
                 offset_seconds: Optional[pulumi.Input[int]] = None,
                 offset_years: Optional[pulumi.Input[int]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumiverse_time as time

        example = time.Offset("example", offset_days=7)
        pulumi.export("oneWeekFromNow", example.rfc3339)
        ```
        ### Triggers Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumiverse_time as time

        ami_update = time.Offset("amiUpdate",
            triggers={
                "ami_id": data["aws_ami"]["example"]["id"],
            },
            offset_days=7)
        server = aws.ec2.Instance("server",
            ami=ami_update.triggers["amiId"],
            tags={
                "ExpirationTime": ami_update.rfc3339,
            })
        # ... (other aws_instance arguments) ...
        ```

        ## Import

        This resource can be imported using the base UTC RFC3339 timestamp and offset years, months, days, hours, minutes, and seconds, separated by commas (`,`), e.g.

        ```sh
         $ pulumi import time:index/offset:Offset example 2020-02-12T06:36:13Z,0,0,7,0,0,0
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_rfc3339: Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OffsetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumiverse_time as time

        example = time.Offset("example", offset_days=7)
        pulumi.export("oneWeekFromNow", example.rfc3339)
        ```
        ### Triggers Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumiverse_time as time

        ami_update = time.Offset("amiUpdate",
            triggers={
                "ami_id": data["aws_ami"]["example"]["id"],
            },
            offset_days=7)
        server = aws.ec2.Instance("server",
            ami=ami_update.triggers["amiId"],
            tags={
                "ExpirationTime": ami_update.rfc3339,
            })
        # ... (other aws_instance arguments) ...
        ```

        ## Import

        This resource can be imported using the base UTC RFC3339 timestamp and offset years, months, days, hours, minutes, and seconds, separated by commas (`,`), e.g.

        ```sh
         $ pulumi import time:index/offset:Offset example 2020-02-12T06:36:13Z,0,0,7,0,0,0
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param OffsetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OffsetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_rfc3339: Optional[pulumi.Input[str]] = None,
                 offset_days: Optional[pulumi.Input[int]] = None,
                 offset_hours: Optional[pulumi.Input[int]] = None,
                 offset_minutes: Optional[pulumi.Input[int]] = None,
                 offset_months: Optional[pulumi.Input[int]] = None,
                 offset_seconds: Optional[pulumi.Input[int]] = None,
                 offset_years: Optional[pulumi.Input[int]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OffsetArgs.__new__(OffsetArgs)

            __props__.__dict__["base_rfc3339"] = base_rfc3339
            __props__.__dict__["offset_days"] = offset_days
            __props__.__dict__["offset_hours"] = offset_hours
            __props__.__dict__["offset_minutes"] = offset_minutes
            __props__.__dict__["offset_months"] = offset_months
            __props__.__dict__["offset_seconds"] = offset_seconds
            __props__.__dict__["offset_years"] = offset_years
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["day"] = None
            __props__.__dict__["hour"] = None
            __props__.__dict__["minute"] = None
            __props__.__dict__["month"] = None
            __props__.__dict__["rfc3339"] = None
            __props__.__dict__["second"] = None
            __props__.__dict__["unix"] = None
            __props__.__dict__["year"] = None
        super(Offset, __self__).__init__(
            'time:index/offset:Offset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_rfc3339: Optional[pulumi.Input[str]] = None,
            day: Optional[pulumi.Input[int]] = None,
            hour: Optional[pulumi.Input[int]] = None,
            minute: Optional[pulumi.Input[int]] = None,
            month: Optional[pulumi.Input[int]] = None,
            offset_days: Optional[pulumi.Input[int]] = None,
            offset_hours: Optional[pulumi.Input[int]] = None,
            offset_minutes: Optional[pulumi.Input[int]] = None,
            offset_months: Optional[pulumi.Input[int]] = None,
            offset_seconds: Optional[pulumi.Input[int]] = None,
            offset_years: Optional[pulumi.Input[int]] = None,
            rfc3339: Optional[pulumi.Input[str]] = None,
            second: Optional[pulumi.Input[int]] = None,
            triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            unix: Optional[pulumi.Input[int]] = None,
            year: Optional[pulumi.Input[int]] = None) -> 'Offset':
        """
        Get an existing Offset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_rfc3339: Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] day: Number day of offset timestamp.
        :param pulumi.Input[int] hour: Number hour of offset timestamp.
        :param pulumi.Input[int] minute: Number minute of offset timestamp.
        :param pulumi.Input[int] month: Number month of offset timestamp.
        :param pulumi.Input[int] offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[int] offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        :param pulumi.Input[str] rfc3339: RFC3339 format of the offset timestamp, e.g. `2020-02-12T06:36:13Z`.
        :param pulumi.Input[int] second: Number second of offset timestamp.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        :param pulumi.Input[int] unix: Number of seconds since epoch time, e.g. `1581489373`.
        :param pulumi.Input[int] year: Number year of offset timestamp.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OffsetState.__new__(_OffsetState)

        __props__.__dict__["base_rfc3339"] = base_rfc3339
        __props__.__dict__["day"] = day
        __props__.__dict__["hour"] = hour
        __props__.__dict__["minute"] = minute
        __props__.__dict__["month"] = month
        __props__.__dict__["offset_days"] = offset_days
        __props__.__dict__["offset_hours"] = offset_hours
        __props__.__dict__["offset_minutes"] = offset_minutes
        __props__.__dict__["offset_months"] = offset_months
        __props__.__dict__["offset_seconds"] = offset_seconds
        __props__.__dict__["offset_years"] = offset_years
        __props__.__dict__["rfc3339"] = rfc3339
        __props__.__dict__["second"] = second
        __props__.__dict__["triggers"] = triggers
        __props__.__dict__["unix"] = unix
        __props__.__dict__["year"] = year
        return Offset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseRfc3339")
    def base_rfc3339(self) -> pulumi.Output[str]:
        """
        Base timestamp in [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) format (see [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) e.g., `YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "base_rfc3339")

    @property
    @pulumi.getter
    def day(self) -> pulumi.Output[int]:
        """
        Number day of offset timestamp.
        """
        return pulumi.get(self, "day")

    @property
    @pulumi.getter
    def hour(self) -> pulumi.Output[int]:
        """
        Number hour of offset timestamp.
        """
        return pulumi.get(self, "hour")

    @property
    @pulumi.getter
    def minute(self) -> pulumi.Output[int]:
        """
        Number minute of offset timestamp.
        """
        return pulumi.get(self, "minute")

    @property
    @pulumi.getter
    def month(self) -> pulumi.Output[int]:
        """
        Number month of offset timestamp.
        """
        return pulumi.get(self, "month")

    @property
    @pulumi.getter(name="offsetDays")
    def offset_days(self) -> pulumi.Output[Optional[int]]:
        """
        Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_days")

    @property
    @pulumi.getter(name="offsetHours")
    def offset_hours(self) -> pulumi.Output[Optional[int]]:
        """
        Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_hours")

    @property
    @pulumi.getter(name="offsetMinutes")
    def offset_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_minutes")

    @property
    @pulumi.getter(name="offsetMonths")
    def offset_months(self) -> pulumi.Output[Optional[int]]:
        """
        Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_months")

    @property
    @pulumi.getter(name="offsetSeconds")
    def offset_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_seconds")

    @property
    @pulumi.getter(name="offsetYears")
    def offset_years(self) -> pulumi.Output[Optional[int]]:
        """
        Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.
        """
        return pulumi.get(self, "offset_years")

    @property
    @pulumi.getter
    def rfc3339(self) -> pulumi.Output[str]:
        """
        RFC3339 format of the offset timestamp, e.g. `2020-02-12T06:36:13Z`.
        """
        return pulumi.get(self, "rfc3339")

    @property
    @pulumi.getter
    def second(self) -> pulumi.Output[int]:
        """
        Number second of offset timestamp.
        """
        return pulumi.get(self, "second")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter
    def unix(self) -> pulumi.Output[int]:
        """
        Number of seconds since epoch time, e.g. `1581489373`.
        """
        return pulumi.get(self, "unix")

    @property
    @pulumi.getter
    def year(self) -> pulumi.Output[int]:
        """
        Number year of offset timestamp.
        """
        return pulumi.get(self, "year")

