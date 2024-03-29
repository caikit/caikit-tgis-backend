# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10generation.proto\x12\x05\x66maas\"\xa1\x01\n\x18\x42\x61tchedGenerationRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x16\n\tprefix_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12*\n\x08requests\x18\x03 \x03(\x0b\x32\x18.fmaas.GenerationRequest\x12!\n\x06params\x18\n \x01(\x0b\x32\x11.fmaas.ParametersB\x0c\n\n_prefix_id\"\x9f\x01\n\x17SingleGenerationRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x16\n\tprefix_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12)\n\x07request\x18\x03 \x01(\x0b\x32\x18.fmaas.GenerationRequest\x12!\n\x06params\x18\n \x01(\x0b\x32\x11.fmaas.ParametersB\x0c\n\n_prefix_id\"I\n\x19\x42\x61tchedGenerationResponse\x12,\n\tresponses\x18\x01 \x03(\x0b\x32\x19.fmaas.GenerationResponse\"!\n\x11GenerationRequest\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xdc\x01\n\x12GenerationResponse\x12\x19\n\x11input_token_count\x18\x06 \x01(\r\x12\x1d\n\x15generated_token_count\x18\x02 \x01(\r\x12\x0c\n\x04text\x18\x04 \x01(\t\x12&\n\x0bstop_reason\x18\x07 \x01(\x0e\x32\x11.fmaas.StopReason\x12\x0c\n\x04seed\x18\n \x01(\x04\x12 \n\x06tokens\x18\x08 \x03(\x0b\x32\x10.fmaas.TokenInfo\x12&\n\x0cinput_tokens\x18\t \x03(\x0b\x32\x10.fmaas.TokenInfo\"\x81\x02\n\nParameters\x12%\n\x06method\x18\x01 \x01(\x0e\x32\x15.fmaas.DecodingMethod\x12+\n\x08sampling\x18\x02 \x01(\x0b\x32\x19.fmaas.SamplingParameters\x12)\n\x08stopping\x18\x03 \x01(\x0b\x32\x17.fmaas.StoppingCriteria\x12(\n\x08response\x18\x04 \x01(\x0b\x32\x16.fmaas.ResponseOptions\x12+\n\x08\x64\x65\x63oding\x18\x05 \x01(\x0b\x32\x19.fmaas.DecodingParameters\x12\x1d\n\x15truncate_input_tokens\x18\x06 \x01(\r\"\xc5\x01\n\x12\x44\x65\x63odingParameters\x12\x1a\n\x12repetition_penalty\x18\x01 \x01(\x02\x12\x44\n\x0elength_penalty\x18\x02 \x01(\x0b\x32\'.fmaas.DecodingParameters.LengthPenaltyH\x00\x88\x01\x01\x1a:\n\rLengthPenalty\x12\x13\n\x0bstart_index\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x65\x63\x61y_factor\x18\x02 \x01(\x02\x42\x11\n\x0f_length_penalty\"v\n\x12SamplingParameters\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\r\n\x05top_k\x18\x02 \x01(\r\x12\r\n\x05top_p\x18\x03 \x01(\x02\x12\x11\n\ttypical_p\x18\x04 \x01(\x02\x12\x11\n\x04seed\x18\x05 \x01(\x04H\x00\x88\x01\x01\x42\x07\n\x05_seed\"u\n\x10StoppingCriteria\x12\x16\n\x0emax_new_tokens\x18\x01 \x01(\r\x12\x16\n\x0emin_new_tokens\x18\x02 \x01(\r\x12\x19\n\x11time_limit_millis\x18\x03 \x01(\r\x12\x16\n\x0estop_sequences\x18\x04 \x03(\t\"\x98\x01\n\x0fResponseOptions\x12\x12\n\ninput_text\x18\x01 \x01(\x08\x12\x18\n\x10generated_tokens\x18\x02 \x01(\x08\x12\x14\n\x0cinput_tokens\x18\x03 \x01(\x08\x12\x16\n\x0etoken_logprobs\x18\x04 \x01(\x08\x12\x13\n\x0btoken_ranks\x18\x05 \x01(\x08\x12\x14\n\x0ctop_n_tokens\x18\x06 \x01(\r\"\x92\x01\n\tTokenInfo\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07logprob\x18\x03 \x01(\x02\x12\x0c\n\x04rank\x18\x04 \x01(\r\x12-\n\ntop_tokens\x18\x05 \x03(\x0b\x32\x19.fmaas.TokenInfo.TopToken\x1a)\n\x08TopToken\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07logprob\x18\x03 \x01(\x02\"k\n\x16\x42\x61tchedTokenizeRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12(\n\x08requests\x18\x02 \x03(\x0b\x32\x16.fmaas.TokenizeRequest\x12\x15\n\rreturn_tokens\x18\x03 \x01(\x08\"E\n\x17\x42\x61tchedTokenizeResponse\x12*\n\tresponses\x18\x01 \x03(\x0b\x32\x17.fmaas.TokenizeResponse\"\x1f\n\x0fTokenizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"7\n\x10TokenizeResponse\x12\x13\n\x0btoken_count\x18\x01 \x01(\r\x12\x0e\n\x06tokens\x18\x02 \x03(\t\"$\n\x10ModelInfoRequest\x12\x10\n\x08model_id\x18\x01 \x01(\t\"\xb4\x01\n\x11ModelInfoResponse\x12\x36\n\nmodel_kind\x18\x01 \x01(\x0e\x32\".fmaas.ModelInfoResponse.ModelKind\x12\x1b\n\x13max_sequence_length\x18\x02 \x01(\r\x12\x16\n\x0emax_new_tokens\x18\x03 \x01(\r\"2\n\tModelKind\x12\x10\n\x0c\x44\x45\x43ODER_ONLY\x10\x00\x12\x13\n\x0f\x45NCODER_DECODER\x10\x01*(\n\x0e\x44\x65\x63odingMethod\x12\n\n\x06GREEDY\x10\x00\x12\n\n\x06SAMPLE\x10\x01*\x8b\x01\n\nStopReason\x12\x10\n\x0cNOT_FINISHED\x10\x00\x12\x0e\n\nMAX_TOKENS\x10\x01\x12\r\n\tEOS_TOKEN\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0e\n\nTIME_LIMIT\x10\x04\x12\x11\n\rSTOP_SEQUENCE\x10\x05\x12\x0f\n\x0bTOKEN_LIMIT\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x32\xc4\x02\n\x11GenerationService\x12O\n\x08Generate\x12\x1f.fmaas.BatchedGenerationRequest\x1a .fmaas.BatchedGenerationResponse\"\x00\x12O\n\x0eGenerateStream\x12\x1e.fmaas.SingleGenerationRequest\x1a\x19.fmaas.GenerationResponse\"\x00\x30\x01\x12K\n\x08Tokenize\x12\x1d.fmaas.BatchedTokenizeRequest\x1a\x1e.fmaas.BatchedTokenizeResponse\"\x00\x12@\n\tModelInfo\x12\x17.fmaas.ModelInfoRequest\x1a\x18.fmaas.ModelInfoResponse\"\x00\x62\x06proto3')

_DECODINGMETHOD = DESCRIPTOR.enum_types_by_name['DecodingMethod']
DecodingMethod = enum_type_wrapper.EnumTypeWrapper(_DECODINGMETHOD)
_STOPREASON = DESCRIPTOR.enum_types_by_name['StopReason']
StopReason = enum_type_wrapper.EnumTypeWrapper(_STOPREASON)
GREEDY = 0
SAMPLE = 1
NOT_FINISHED = 0
MAX_TOKENS = 1
EOS_TOKEN = 2
CANCELLED = 3
TIME_LIMIT = 4
STOP_SEQUENCE = 5
TOKEN_LIMIT = 6
ERROR = 7


_BATCHEDGENERATIONREQUEST = DESCRIPTOR.message_types_by_name['BatchedGenerationRequest']
_SINGLEGENERATIONREQUEST = DESCRIPTOR.message_types_by_name['SingleGenerationRequest']
_BATCHEDGENERATIONRESPONSE = DESCRIPTOR.message_types_by_name['BatchedGenerationResponse']
_GENERATIONREQUEST = DESCRIPTOR.message_types_by_name['GenerationRequest']
_GENERATIONRESPONSE = DESCRIPTOR.message_types_by_name['GenerationResponse']
_PARAMETERS = DESCRIPTOR.message_types_by_name['Parameters']
_DECODINGPARAMETERS = DESCRIPTOR.message_types_by_name['DecodingParameters']
_DECODINGPARAMETERS_LENGTHPENALTY = _DECODINGPARAMETERS.nested_types_by_name['LengthPenalty']
_SAMPLINGPARAMETERS = DESCRIPTOR.message_types_by_name['SamplingParameters']
_STOPPINGCRITERIA = DESCRIPTOR.message_types_by_name['StoppingCriteria']
_RESPONSEOPTIONS = DESCRIPTOR.message_types_by_name['ResponseOptions']
_TOKENINFO = DESCRIPTOR.message_types_by_name['TokenInfo']
_TOKENINFO_TOPTOKEN = _TOKENINFO.nested_types_by_name['TopToken']
_BATCHEDTOKENIZEREQUEST = DESCRIPTOR.message_types_by_name['BatchedTokenizeRequest']
_BATCHEDTOKENIZERESPONSE = DESCRIPTOR.message_types_by_name['BatchedTokenizeResponse']
_TOKENIZEREQUEST = DESCRIPTOR.message_types_by_name['TokenizeRequest']
_TOKENIZERESPONSE = DESCRIPTOR.message_types_by_name['TokenizeResponse']
_MODELINFOREQUEST = DESCRIPTOR.message_types_by_name['ModelInfoRequest']
_MODELINFORESPONSE = DESCRIPTOR.message_types_by_name['ModelInfoResponse']
_MODELINFORESPONSE_MODELKIND = _MODELINFORESPONSE.enum_types_by_name['ModelKind']
BatchedGenerationRequest = _reflection.GeneratedProtocolMessageType('BatchedGenerationRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHEDGENERATIONREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.BatchedGenerationRequest)
  })
_sym_db.RegisterMessage(BatchedGenerationRequest)

SingleGenerationRequest = _reflection.GeneratedProtocolMessageType('SingleGenerationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEGENERATIONREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.SingleGenerationRequest)
  })
_sym_db.RegisterMessage(SingleGenerationRequest)

BatchedGenerationResponse = _reflection.GeneratedProtocolMessageType('BatchedGenerationResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHEDGENERATIONRESPONSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.BatchedGenerationResponse)
  })
_sym_db.RegisterMessage(BatchedGenerationResponse)

GenerationRequest = _reflection.GeneratedProtocolMessageType('GenerationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATIONREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.GenerationRequest)
  })
_sym_db.RegisterMessage(GenerationRequest)

GenerationResponse = _reflection.GeneratedProtocolMessageType('GenerationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATIONRESPONSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.GenerationResponse)
  })
_sym_db.RegisterMessage(GenerationResponse)

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.Parameters)
  })
_sym_db.RegisterMessage(Parameters)

DecodingParameters = _reflection.GeneratedProtocolMessageType('DecodingParameters', (_message.Message,), {

  'LengthPenalty' : _reflection.GeneratedProtocolMessageType('LengthPenalty', (_message.Message,), {
    'DESCRIPTOR' : _DECODINGPARAMETERS_LENGTHPENALTY,
    '__module__' : 'generation_pb2'
    # @@protoc_insertion_point(class_scope:fmaas.DecodingParameters.LengthPenalty)
    })
  ,
  'DESCRIPTOR' : _DECODINGPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.DecodingParameters)
  })
_sym_db.RegisterMessage(DecodingParameters)
_sym_db.RegisterMessage(DecodingParameters.LengthPenalty)

SamplingParameters = _reflection.GeneratedProtocolMessageType('SamplingParameters', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLINGPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.SamplingParameters)
  })
_sym_db.RegisterMessage(SamplingParameters)

StoppingCriteria = _reflection.GeneratedProtocolMessageType('StoppingCriteria', (_message.Message,), {
  'DESCRIPTOR' : _STOPPINGCRITERIA,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.StoppingCriteria)
  })
_sym_db.RegisterMessage(StoppingCriteria)

ResponseOptions = _reflection.GeneratedProtocolMessageType('ResponseOptions', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEOPTIONS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.ResponseOptions)
  })
_sym_db.RegisterMessage(ResponseOptions)

TokenInfo = _reflection.GeneratedProtocolMessageType('TokenInfo', (_message.Message,), {

  'TopToken' : _reflection.GeneratedProtocolMessageType('TopToken', (_message.Message,), {
    'DESCRIPTOR' : _TOKENINFO_TOPTOKEN,
    '__module__' : 'generation_pb2'
    # @@protoc_insertion_point(class_scope:fmaas.TokenInfo.TopToken)
    })
  ,
  'DESCRIPTOR' : _TOKENINFO,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.TokenInfo)
  })
_sym_db.RegisterMessage(TokenInfo)
_sym_db.RegisterMessage(TokenInfo.TopToken)

BatchedTokenizeRequest = _reflection.GeneratedProtocolMessageType('BatchedTokenizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHEDTOKENIZEREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.BatchedTokenizeRequest)
  })
_sym_db.RegisterMessage(BatchedTokenizeRequest)

BatchedTokenizeResponse = _reflection.GeneratedProtocolMessageType('BatchedTokenizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHEDTOKENIZERESPONSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.BatchedTokenizeResponse)
  })
_sym_db.RegisterMessage(BatchedTokenizeResponse)

TokenizeRequest = _reflection.GeneratedProtocolMessageType('TokenizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOKENIZEREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.TokenizeRequest)
  })
_sym_db.RegisterMessage(TokenizeRequest)

TokenizeResponse = _reflection.GeneratedProtocolMessageType('TokenizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENIZERESPONSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.TokenizeResponse)
  })
_sym_db.RegisterMessage(TokenizeResponse)

ModelInfoRequest = _reflection.GeneratedProtocolMessageType('ModelInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFOREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.ModelInfoRequest)
  })
_sym_db.RegisterMessage(ModelInfoRequest)

ModelInfoResponse = _reflection.GeneratedProtocolMessageType('ModelInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFORESPONSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:fmaas.ModelInfoResponse)
  })
_sym_db.RegisterMessage(ModelInfoResponse)

_GENERATIONSERVICE = DESCRIPTOR.services_by_name['GenerationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DECODINGMETHOD._serialized_start=2180
  _DECODINGMETHOD._serialized_end=2220
  _STOPREASON._serialized_start=2223
  _STOPREASON._serialized_end=2362
  _BATCHEDGENERATIONREQUEST._serialized_start=28
  _BATCHEDGENERATIONREQUEST._serialized_end=189
  _SINGLEGENERATIONREQUEST._serialized_start=192
  _SINGLEGENERATIONREQUEST._serialized_end=351
  _BATCHEDGENERATIONRESPONSE._serialized_start=353
  _BATCHEDGENERATIONRESPONSE._serialized_end=426
  _GENERATIONREQUEST._serialized_start=428
  _GENERATIONREQUEST._serialized_end=461
  _GENERATIONRESPONSE._serialized_start=464
  _GENERATIONRESPONSE._serialized_end=684
  _PARAMETERS._serialized_start=687
  _PARAMETERS._serialized_end=944
  _DECODINGPARAMETERS._serialized_start=947
  _DECODINGPARAMETERS._serialized_end=1144
  _DECODINGPARAMETERS_LENGTHPENALTY._serialized_start=1067
  _DECODINGPARAMETERS_LENGTHPENALTY._serialized_end=1125
  _SAMPLINGPARAMETERS._serialized_start=1146
  _SAMPLINGPARAMETERS._serialized_end=1264
  _STOPPINGCRITERIA._serialized_start=1266
  _STOPPINGCRITERIA._serialized_end=1383
  _RESPONSEOPTIONS._serialized_start=1386
  _RESPONSEOPTIONS._serialized_end=1538
  _TOKENINFO._serialized_start=1541
  _TOKENINFO._serialized_end=1687
  _TOKENINFO_TOPTOKEN._serialized_start=1646
  _TOKENINFO_TOPTOKEN._serialized_end=1687
  _BATCHEDTOKENIZEREQUEST._serialized_start=1689
  _BATCHEDTOKENIZEREQUEST._serialized_end=1796
  _BATCHEDTOKENIZERESPONSE._serialized_start=1798
  _BATCHEDTOKENIZERESPONSE._serialized_end=1867
  _TOKENIZEREQUEST._serialized_start=1869
  _TOKENIZEREQUEST._serialized_end=1900
  _TOKENIZERESPONSE._serialized_start=1902
  _TOKENIZERESPONSE._serialized_end=1957
  _MODELINFOREQUEST._serialized_start=1959
  _MODELINFOREQUEST._serialized_end=1995
  _MODELINFORESPONSE._serialized_start=1998
  _MODELINFORESPONSE._serialized_end=2178
  _MODELINFORESPONSE_MODELKIND._serialized_start=2128
  _MODELINFORESPONSE_MODELKIND._serialized_end=2178
  _GENERATIONSERVICE._serialized_start=2365
  _GENERATIONSERVICE._serialized_end=2689
# @@protoc_insertion_point(module_scope)
