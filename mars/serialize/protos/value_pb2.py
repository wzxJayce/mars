# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mars/serialize/protos/value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mars/serialize/protos/value.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!mars/serialize/protos/value.proto\"\xde\x04\n\x05Value\x12\x11\n\x07is_null\x18\x01 \x01(\x08H\x00\x12\x0b\n\x01\x62\x18\x02 \x01(\x08H\x00\x12\x0b\n\x01i\x18\x03 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01s\x18\x05 \x01(\x0cH\x00\x12\x0b\n\x01u\x18\x06 \x01(\tH\x00\x12\x1b\n\x04list\x18\x07 \x01(\x0b\x32\x0b.Value.ListH\x00\x12\x1b\n\x04\x64ict\x18\x08 \x01(\x0b\x32\x0b.Value.DictH\x00\x12\x1d\n\x05slice\x18\t \x01(\x0b\x32\x0c.Value.SliceH\x00\x12\r\n\x03\x61rr\x18\n \x01(\x0cH\x00\x12\x0f\n\x05\x64type\x18\x0b \x01(\x0cH\x00\x12\x19\n\x03key\x18\x0c \x01(\x0b\x32\n.Value.KeyH\x00\x12\x14\n\ndatetime64\x18\r \x01(\x0cH\x00\x12\x15\n\x0btimedelta64\x18\x0e \x01(\x0cH\x00\x12\x0f\n\x05index\x18\x0f \x01(\x0cH\x00\x12\x10\n\x06series\x18\x10 \x01(\x0cH\x00\x12\x13\n\tdataframe\x18\x11 \x01(\x0cH\x00\x1a/\n\x04List\x12\x10\n\x08is_tuple\x18\x01 \x01(\x08\x12\x15\n\x05value\x18\x02 \x03(\x0b\x32\x06.Value\x1an\n\x05Slice\x12\x0f\n\x07is_null\x18\x04 \x01(\x08\x12\x13\n\tstart_val\x18\x01 \x01(\x03H\x00\x12\x12\n\x08stop_val\x18\x02 \x01(\x03H\x01\x12\x12\n\x08step_val\x18\x03 \x01(\x03H\x02\x42\x07\n\x05startB\x06\n\x04stopB\x06\n\x04step\x1a>\n\x04\x44ict\x12\x19\n\x04keys\x18\x01 \x01(\x0b\x32\x0b.Value.List\x12\x1b\n\x06values\x18\x02 \x01(\x0b\x32\x0b.Value.List\x1a\x1e\n\x03Key\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\tB\x07\n\x05valueb\x06proto3')
)




_VALUE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='Value.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_tuple', full_name='Value.List.is_tuple', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Value.List.value', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=427,
)

_VALUE_SLICE = _descriptor.Descriptor(
  name='Slice',
  full_name='Value.Slice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_null', full_name='Value.Slice.is_null', index=0,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_val', full_name='Value.Slice.start_val', index=1,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_val', full_name='Value.Slice.stop_val', index=2,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step_val', full_name='Value.Slice.step_val', index=3,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='start', full_name='Value.Slice.start',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='stop', full_name='Value.Slice.stop',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='step', full_name='Value.Slice.step',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=429,
  serialized_end=539,
)

_VALUE_DICT = _descriptor.Descriptor(
  name='Dict',
  full_name='Value.Dict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='Value.Dict.keys', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='Value.Dict.values', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=603,
)

_VALUE_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='Value.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Value.Key.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Value.Key.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=635,
)

_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_null', full_name='Value.is_null', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='Value.b', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='Value.i', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='Value.f', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s', full_name='Value.s', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='u', full_name='Value.u', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='Value.list', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dict', full_name='Value.dict', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slice', full_name='Value.slice', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arr', full_name='Value.arr', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='Value.dtype', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='Value.key', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datetime64', full_name='Value.datetime64', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timedelta64', full_name='Value.timedelta64', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='Value.index', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='series', full_name='Value.series', index=15,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataframe', full_name='Value.dataframe', index=16,
      number=17, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VALUE_LIST, _VALUE_SLICE, _VALUE_DICT, _VALUE_KEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='Value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=38,
  serialized_end=644,
)

_VALUE_LIST.fields_by_name['value'].message_type = _VALUE
_VALUE_LIST.containing_type = _VALUE
_VALUE_SLICE.containing_type = _VALUE
_VALUE_SLICE.oneofs_by_name['start'].fields.append(
  _VALUE_SLICE.fields_by_name['start_val'])
_VALUE_SLICE.fields_by_name['start_val'].containing_oneof = _VALUE_SLICE.oneofs_by_name['start']
_VALUE_SLICE.oneofs_by_name['stop'].fields.append(
  _VALUE_SLICE.fields_by_name['stop_val'])
_VALUE_SLICE.fields_by_name['stop_val'].containing_oneof = _VALUE_SLICE.oneofs_by_name['stop']
_VALUE_SLICE.oneofs_by_name['step'].fields.append(
  _VALUE_SLICE.fields_by_name['step_val'])
_VALUE_SLICE.fields_by_name['step_val'].containing_oneof = _VALUE_SLICE.oneofs_by_name['step']
_VALUE_DICT.fields_by_name['keys'].message_type = _VALUE_LIST
_VALUE_DICT.fields_by_name['values'].message_type = _VALUE_LIST
_VALUE_DICT.containing_type = _VALUE
_VALUE_KEY.containing_type = _VALUE
_VALUE.fields_by_name['list'].message_type = _VALUE_LIST
_VALUE.fields_by_name['dict'].message_type = _VALUE_DICT
_VALUE.fields_by_name['slice'].message_type = _VALUE_SLICE
_VALUE.fields_by_name['key'].message_type = _VALUE_KEY
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['is_null'])
_VALUE.fields_by_name['is_null'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['b'])
_VALUE.fields_by_name['b'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['i'])
_VALUE.fields_by_name['i'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['f'])
_VALUE.fields_by_name['f'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['s'])
_VALUE.fields_by_name['s'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['u'])
_VALUE.fields_by_name['u'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['list'])
_VALUE.fields_by_name['list'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['dict'])
_VALUE.fields_by_name['dict'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['slice'])
_VALUE.fields_by_name['slice'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['arr'])
_VALUE.fields_by_name['arr'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['dtype'])
_VALUE.fields_by_name['dtype'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['key'])
_VALUE.fields_by_name['key'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['datetime64'])
_VALUE.fields_by_name['datetime64'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['timedelta64'])
_VALUE.fields_by_name['timedelta64'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['index'])
_VALUE.fields_by_name['index'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['series'])
_VALUE.fields_by_name['series'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['dataframe'])
_VALUE.fields_by_name['dataframe'].containing_oneof = _VALUE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_LIST,
    __module__ = 'mars.serialize.protos.value_pb2'
    # @@protoc_insertion_point(class_scope:Value.List)
    ))
  ,

  Slice = _reflection.GeneratedProtocolMessageType('Slice', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_SLICE,
    __module__ = 'mars.serialize.protos.value_pb2'
    # @@protoc_insertion_point(class_scope:Value.Slice)
    ))
  ,

  Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_DICT,
    __module__ = 'mars.serialize.protos.value_pb2'
    # @@protoc_insertion_point(class_scope:Value.Dict)
    ))
  ,

  Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_KEY,
    __module__ = 'mars.serialize.protos.value_pb2'
    # @@protoc_insertion_point(class_scope:Value.Key)
    ))
  ,
  DESCRIPTOR = _VALUE,
  __module__ = 'mars.serialize.protos.value_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  ))
_sym_db.RegisterMessage(Value)
_sym_db.RegisterMessage(Value.List)
_sym_db.RegisterMessage(Value.Slice)
_sym_db.RegisterMessage(Value.Dict)
_sym_db.RegisterMessage(Value.Key)


# @@protoc_insertion_point(module_scope)
