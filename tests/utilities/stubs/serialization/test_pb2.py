# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialization/test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ni_measurementlink_service._internal.stubs.ni.protobuf.types import xydata_pb2 as ni_dot_protobuf_dot_types_dot_xydata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18serialization/test.proto\x12\x32ni.measurementlink.measurement.tests.serialization\x1a\x1eni/protobuf/types/xydata.proto\"\xdc\x06\n\x14MeasurementParameter\x12\x12\n\nfloat_data\x18\x01 \x01(\x02\x12\x13\n\x0b\x64ouble_data\x18\x02 \x01(\x01\x12\x12\n\nint32_data\x18\x03 \x01(\x05\x12\x13\n\x0buint32_data\x18\x04 \x01(\r\x12\x12\n\nint64_data\x18\x05 \x01(\x03\x12\x13\n\x0buint64_data\x18\x06 \x01(\x04\x12\x11\n\tbool_data\x18\x07 \x01(\x08\x12\x13\n\x0bstring_data\x18\x08 \x01(\t\x12\x19\n\x11\x64ouble_array_data\x18\t \x03(\x01\x12\x18\n\x10\x66loat_array_data\x18\n \x03(\x02\x12\x18\n\x10int32_array_data\x18\x0b \x03(\x05\x12\x19\n\x11uint32_array_data\x18\x0c \x03(\r\x12\x18\n\x10int64_array_data\x18\r \x03(\x03\x12\x19\n\x11uint64_array_data\x18\x0e \x03(\x04\x12\x17\n\x0f\x62ool_array_data\x18\x0f \x03(\x08\x12\x19\n\x11string_array_data\x18\x10 \x03(\t\x12U\n\tenum_data\x18\x11 \x01(\x0e\x32\x42.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12[\n\x0f\x65num_array_data\x18\x12 \x03(\x0e\x32\x42.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12T\n\rint_enum_data\x18\x13 \x01(\x0e\x32=.ni.measurementlink.measurement.tests.serialization.Countries\x12Z\n\x13int_enum_array_data\x18\x14 \x03(\x0e\x32=.ni.measurementlink.measurement.tests.serialization.Countries\x12\x30\n\x07xy_data\x18\x15 \x01(\x0b\x32\x1f.ni.protobuf.types.DoubleXYData\x12\x36\n\rxy_data_array\x18\x16 \x03(\x0b\x32\x1f.ni.protobuf.types.DoubleXYData*=\n\x0e\x44ifferentColor\x12\n\n\x06PURPLE\x10\x00\x12\n\n\x06ORANGE\x10\x01\x12\x08\n\x04TEAL\x10\x02\x12\t\n\x05\x42ROWN\x10\x03*?\n\tCountries\x12\x0b\n\x07\x41MERICA\x10\x00\x12\n\n\x06TAIWAN\x10\x01\x12\r\n\tAUSTRALIA\x10\x02\x12\n\n\x06\x43\x41NADA\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serialization.test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DIFFERENTCOLOR._serialized_start=975
  _DIFFERENTCOLOR._serialized_end=1036
  _COUNTRIES._serialized_start=1038
  _COUNTRIES._serialized_end=1101
  _MEASUREMENTPARAMETER._serialized_start=113
  _MEASUREMENTPARAMETER._serialized_end=973
# @@protoc_insertion_point(module_scope)
