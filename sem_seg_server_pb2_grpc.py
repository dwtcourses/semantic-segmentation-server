# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sem_seg_server_pb2 as sem__seg__server__pb2


class SemanticSegmentationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSegmentedObjects = channel.unary_unary(
        '/sem_seg_server.SemanticSegmentation/GetSegmentedObjects',
        request_serializer=sem__seg__server__pb2.Empty.SerializeToString,
        response_deserializer=sem__seg__server__pb2.SegmentedObjectData.FromString,
        )
    self.GetCameraResolution = channel.unary_unary(
        '/sem_seg_server.SemanticSegmentation/GetCameraResolution',
        request_serializer=sem__seg__server__pb2.Empty.SerializeToString,
        response_deserializer=sem__seg__server__pb2.CameraResolution.FromString,
        )


class SemanticSegmentationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSegmentedObjects(self, request, context):
    """A simple RPC. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCameraResolution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SemanticSegmentationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSegmentedObjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetSegmentedObjects,
          request_deserializer=sem__seg__server__pb2.Empty.FromString,
          response_serializer=sem__seg__server__pb2.SegmentedObjectData.SerializeToString,
      ),
      'GetCameraResolution': grpc.unary_unary_rpc_method_handler(
          servicer.GetCameraResolution,
          request_deserializer=sem__seg__server__pb2.Empty.FromString,
          response_serializer=sem__seg__server__pb2.CameraResolution.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sem_seg_server.SemanticSegmentation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
