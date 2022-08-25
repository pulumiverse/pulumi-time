# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .time_offset import *
from .time_rotating import *
from .time_static import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "time",
  "mod": "index/timeOffset",
  "fqn": "pulumiverse_time",
  "classes": {
   "time:index/timeOffset:TimeOffset": "TimeOffset"
  }
 },
 {
  "pkg": "time",
  "mod": "index/timeRotating",
  "fqn": "pulumiverse_time",
  "classes": {
   "time:index/timeRotating:TimeRotating": "TimeRotating"
  }
 },
 {
  "pkg": "time",
  "mod": "index/timeStatic",
  "fqn": "pulumiverse_time",
  "classes": {
   "time:index/timeStatic:TimeStatic": "TimeStatic"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "time",
  "token": "pulumi:providers:time",
  "fqn": "pulumiverse_time",
  "class": "Provider"
 }
]
"""
)
