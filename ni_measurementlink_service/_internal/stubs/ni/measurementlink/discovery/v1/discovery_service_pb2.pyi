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
class ServiceDescriptor(google.protobuf.message.Message):
    """Description of a registered service. This information can be used to display information to the user
    about the service when services are being developed for a plugin architecture
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class AnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_URL_FIELD_NUMBER: builtins.int
    PROVIDED_INTERFACES_FIELD_NUMBER: builtins.int
    SERVICE_CLASS_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    display_name: builtins.str
    """Required. The user visible name of the service."""
    description_url: builtins.str
    """Optional. Url which provides descriptive information about the service"""
    service_class: builtins.str
    """Required. The "class" of a service. The value of this field should be unique for a given interface in provided_interfaces.
    In effect, the .proto service declaration defines the interface, and this field defines a class or concrete type of the interface.
    """
    @property
    def provided_interfaces(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Required. The service interfaces provided by the service. This is the gRPC Full Name of the service.
        Registration can use the gRPC metadata to provide these names.
        """

    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Optional. Represents a set of annotations on the service.
        Well-known annotations:
        - Description
          - Key: "ni/service.description"
          - Expected format: string
          - Example: "Measure inrush current with a shorted load and validate results against configured limits."
        - Collection
          - Key: "ni/service.collection"
          - Expected format: "." delimited namespace/hierarchy case-insensitive string
          - Example: "CurrentTests.Inrush"
        - Tags
          - Key: "ni/service.tags"
          - Expected format: serialized JSON string of an array of strings
          - Example: "[\\"powerup\\", \\"current\\"]"
        """

    def __init__(
        self,
        *,
        display_name: builtins.str = ...,
        description_url: builtins.str = ...,
        provided_interfaces: collections.abc.Iterable[builtins.str] | None = ...,
        service_class: builtins.str = ...,
        annotations: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["annotations", b"annotations", "description_url", b"description_url", "display_name", b"display_name", "provided_interfaces", b"provided_interfaces", "service_class", b"service_class"]) -> None: ...

global___ServiceDescriptor = ServiceDescriptor

@typing.final
class ServiceLocation(google.protobuf.message.Message):
    """Represents the location of a service. The location generally includes the IP address and port number for the service
    which can be used to establish communication with the service.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_FIELD_NUMBER: builtins.int
    INSECURE_PORT_FIELD_NUMBER: builtins.int
    SSL_AUTHENTICATED_PORT_FIELD_NUMBER: builtins.int
    location: builtins.str
    """Required: The location of the service. This is typically an IP address or DNS name."""
    insecure_port: builtins.str
    """The port to use when communicating with the service for insecure HTTP connections. At least one of insecure_port or
    ssl_authenticated_port is required.
    """
    ssl_authenticated_port: builtins.str
    """The port to use when communicating with the service for secure SSL authenticated connections. At least one of
    insecure_port or ssl_authenticated_port is required.
    """
    def __init__(
        self,
        *,
        location: builtins.str = ...,
        insecure_port: builtins.str = ...,
        ssl_authenticated_port: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["insecure_port", b"insecure_port", "location", b"location", "ssl_authenticated_port", b"ssl_authenticated_port"]) -> None: ...

global___ServiceLocation = ServiceLocation

@typing.final
class RegisterServiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_DESCRIPTION_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    @property
    def service_description(self) -> global___ServiceDescriptor:
        """Required. The description of the service."""

    @property
    def location(self) -> global___ServiceLocation:
        """Required. The canonical location information for the service."""

    def __init__(
        self,
        *,
        service_description: global___ServiceDescriptor | None = ...,
        location: global___ServiceLocation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["location", b"location", "service_description", b"service_description"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["location", b"location", "service_description", b"service_description"]) -> None: ...

global___RegisterServiceRequest = RegisterServiceRequest

@typing.final
class RegisterServiceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRATION_ID_FIELD_NUMBER: builtins.int
    registration_id: builtins.str
    """ID that can be used to unregister the service."""
    def __init__(
        self,
        *,
        registration_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["registration_id", b"registration_id"]) -> None: ...

global___RegisterServiceResponse = RegisterServiceResponse

@typing.final
class UnregisterServiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRATION_ID_FIELD_NUMBER: builtins.int
    registration_id: builtins.str
    """Required. The registration ID of the service that should be unregistered."""
    def __init__(
        self,
        *,
        registration_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["registration_id", b"registration_id"]) -> None: ...

global___UnregisterServiceRequest = UnregisterServiceRequest

@typing.final
class UnregisterServiceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnregisterServiceResponse = UnregisterServiceResponse

@typing.final
class EnumerateServicesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROVIDED_INTERFACE_FIELD_NUMBER: builtins.int
    provided_interface: builtins.str
    """Optional. The gRPC full name of the service interface that is needed. If empty,
    information for all services registered with the discovery service will be returned.
    """
    def __init__(
        self,
        *,
        provided_interface: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["provided_interface", b"provided_interface"]) -> None: ...

global___EnumerateServicesRequest = EnumerateServicesRequest

@typing.final
class EnumerateServicesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AVAILABLE_SERVICES_FIELD_NUMBER: builtins.int
    UNREACHABLE_FIELD_NUMBER: builtins.int
    @property
    def available_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceDescriptor]:
        """The list of available services which implement the specified service interface."""

    @property
    def unreachable(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Information about any unreachable resources. Each string in the list will be a
        'ServiceDescriptor.service_class' entry for each of the unreachable resources.
        To get extended information about the unreachable resources, use ResolveService
        and handle the resulting error.
        """

    def __init__(
        self,
        *,
        available_services: collections.abc.Iterable[global___ServiceDescriptor] | None = ...,
        unreachable: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["available_services", b"available_services", "unreachable", b"unreachable"]) -> None: ...

global___EnumerateServicesResponse = EnumerateServicesResponse

@typing.final
class ResolveServiceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROVIDED_INTERFACE_FIELD_NUMBER: builtins.int
    SERVICE_CLASS_FIELD_NUMBER: builtins.int
    DEPLOYMENT_TARGET_FIELD_NUMBER: builtins.int
    provided_interface: builtins.str
    """Required. This corresponds to the gRPC Full Name of the service and should match the information
    that was supplied in the RegisterServiceRequest message.
    """
    service_class: builtins.str
    """Optional. The service "class" that should be matched. If the value of this field is not specified and there
    is more than one matching service registered, an error is returned.
    """
    deployment_target: builtins.str
    """Optional. Indicates the deployment target from which the service should be resolved.
    The value of this field can be obtained from the results of the EnumerateComputeNodes method.
    If the value of this field is not specified, the service will be resolved from the
    local deployment target.  If the service cannot be resolved from the specified deployment
    target, an error is returned.
    """
    def __init__(
        self,
        *,
        provided_interface: builtins.str = ...,
        service_class: builtins.str = ...,
        deployment_target: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deployment_target", b"deployment_target", "provided_interface", b"provided_interface", "service_class", b"service_class"]) -> None: ...

global___ResolveServiceRequest = ResolveServiceRequest

@typing.final
class ComputeNodeDescriptor(google.protobuf.message.Message):
    """Represents a location capable resolving and running a service."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    IS_LOCAL_FIELD_NUMBER: builtins.int
    url: builtins.str
    """The resolvable name of the compute node."""
    is_local: builtins.bool
    """indicates whether the compute node is considered the local node."""
    def __init__(
        self,
        *,
        url: builtins.str = ...,
        is_local: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["is_local", b"is_local", "url", b"url"]) -> None: ...

global___ComputeNodeDescriptor = ComputeNodeDescriptor

@typing.final
class EnumerateComputeNodesRequest(google.protobuf.message.Message):
    """Message sent to enumerate the compute nodes that have registered themselves in the current session."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___EnumerateComputeNodesRequest = EnumerateComputeNodesRequest

@typing.final
class EnumerateComputeNodesResponse(google.protobuf.message.Message):
    """Message returned from the EnumerateComputeNodes method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_NODES_FIELD_NUMBER: builtins.int
    @property
    def compute_nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeNodeDescriptor]:
        """The list of compute nodes that have registered themselves in the current session."""

    def __init__(
        self,
        *,
        compute_nodes: collections.abc.Iterable[global___ComputeNodeDescriptor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_nodes", b"compute_nodes"]) -> None: ...

global___EnumerateComputeNodesResponse = EnumerateComputeNodesResponse
