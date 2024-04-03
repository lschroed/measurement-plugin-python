"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DoubleXYData(google.protobuf.message.Message):
    """XYData for a cartesian graph.
    x_data and y_data should contain the same number of values.
    If they do not, the smaller-sized array will be used to determine
    the number of XY points.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_DATA_FIELD_NUMBER: builtins.int
    Y_DATA_FIELD_NUMBER: builtins.int
    @property
    def x_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def y_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        x_data: collections.abc.Iterable[builtins.float] | None = ...,
        y_data: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["x_data", b"x_data", "y_data", b"y_data"]) -> None: ...

global___DoubleXYData = DoubleXYData
