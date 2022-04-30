# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10users/user.proto\x12\x04user\"K\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\"\x18\n\nGetPayload\x12\n\n\x02id\x18\x01 \x01(\x03\"\x07\n\x05\x45mpty2^\n\x0bUserService\x12\'\n\x07GetUser\x12\x10.user.GetPayload\x1a\n.user.User\x12&\n\tListUsers\x12\x0b.user.Empty\x1a\n.user.User0\x01\x62\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_GETPAYLOAD = DESCRIPTOR.message_types_by_name['GetPayload']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'users.user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)

GetPayload = _reflection.GeneratedProtocolMessageType('GetPayload', (_message.Message,), {
  'DESCRIPTOR' : _GETPAYLOAD,
  '__module__' : 'users.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetPayload)
  })
_sym_db.RegisterMessage(GetPayload)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'users.user_pb2'
  # @@protoc_insertion_point(class_scope:user.Empty)
  })
_sym_db.RegisterMessage(Empty)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=26
  _USER._serialized_end=101
  _GETPAYLOAD._serialized_start=103
  _GETPAYLOAD._serialized_end=127
  _EMPTY._serialized_start=129
  _EMPTY._serialized_end=136
  _USERSERVICE._serialized_start=138
  _USERSERVICE._serialized_end=232
# @@protoc_insertion_point(module_scope)
