# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamingdata/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19streamingdata/types.proto\x12\x32ni.measurementlink.measurement.tests.streamingdata\"\x9a\x01\n\x0e\x43onfigurations\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_responses\x18\x02 \x01(\x05\x12\x11\n\tdata_size\x18\x03 \x01(\x05\x12\x17\n\x0f\x63umulative_data\x18\x04 \x01(\x08\x12\x1f\n\x17response_interval_in_ms\x18\x05 \x01(\x05\x12\x16\n\x0e\x65rror_on_index\x18\x06 \x01(\x05\"4\n\x07Outputs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamingdata.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=82
  _CONFIGURATIONS._serialized_end=236
  _OUTPUTS._serialized_start=238
  _OUTPUTS._serialized_end=290
# @@protoc_insertion_point(module_scope)
