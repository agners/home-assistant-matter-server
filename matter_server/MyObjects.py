import typing
from dataclasses import dataclass, field
from enum import IntEnum

from chip import ChipUtility
from chip.tlv import float32, uint

from .MyClusterObjects import (Cluster, ClusterAttributeDescriptor,
                               ClusterCommand, ClusterEvent, ClusterObject,
                               ClusterObjectDescriptor,
                               ClusterObjectFieldDescriptor)
from .MyTypes import Nullable, NullValue


@dataclass
class OnOff(Cluster):
    id: typing.ClassVar[int] = 0x0006

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields = [
                ClusterObjectFieldDescriptor(Label="onOff", Tag=0x00000000, Type=bool),
                ClusterObjectFieldDescriptor(Label="globalSceneControl", Tag=0x00004000, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="onTime", Tag=0x00004001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="offWaitTime", Tag=0x00004002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="startUpOnOff", Tag=0x00004003, Type=typing.Union[None, Nullable, OnOff.Enums.OnOffStartUpOnOff]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    onOff: 'bool' = None
    globalSceneControl: 'typing.Optional[bool]' = None
    onTime: 'typing.Optional[uint]' = None
    offWaitTime: 'typing.Optional[uint]' = None
    startUpOnOff: 'typing.Union[None, Nullable, OnOff.Enums.OnOffStartUpOnOff]' = None
    generatedCommandList: 'typing.List[uint]' = None
    acceptedCommandList: 'typing.List[uint]' = None
    attributeList: 'typing.List[uint]' = None
    featureMap: 'typing.Optional[uint]' = None
    clusterRevision: 'uint' = None

    class Enums:
        class OnOffDelayedAllOffEffectVariant(IntEnum):
            kFadeToOffIn0p8Seconds = 0x00
            kNoFade = 0x01
            k50PercentDimDownIn0p8SecondsThenFadeToOffIn12Seconds = 0x02

        class OnOffDyingLightEffectVariant(IntEnum):
            k20PercenterDimUpIn0p5SecondsThenFadeToOffIn1Second = 0x00

        class OnOffEffectIdentifier(IntEnum):
            kDelayedAllOff = 0x00
            kDyingLight = 0x01

        class OnOffStartUpOnOff(IntEnum):
            kOff = 0x00
            kOn = 0x01
            kTogglePreviousOnOff = 0x02



    class Commands:
        @dataclass
        class Off(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0000
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                    ])


        @dataclass
        class On(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0001
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                    ])


        @dataclass
        class Toggle(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0002
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                    ])


        @dataclass
        class OffWithEffect(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0040
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                            ClusterObjectFieldDescriptor(Label="effectId", Tag=0, Type=OnOff.Enums.OnOffEffectIdentifier),
                            ClusterObjectFieldDescriptor(Label="effectVariant", Tag=1, Type=OnOff.Enums.OnOffDelayedAllOffEffectVariant),
                    ])

            effectId: 'OnOff.Enums.OnOffEffectIdentifier' = 0
            effectVariant: 'OnOff.Enums.OnOffDelayedAllOffEffectVariant' = 0

        @dataclass
        class OnWithRecallGlobalScene(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0041
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                    ])


        @dataclass
        class OnWithTimedOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0006
            command_id: typing.ClassVar[int] = 0x0042
            is_client: typing.ClassVar[bool] = True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields = [
                            ClusterObjectFieldDescriptor(Label="onOffControl", Tag=0, Type=uint),
                            ClusterObjectFieldDescriptor(Label="onTime", Tag=1, Type=uint),
                            ClusterObjectFieldDescriptor(Label="offWaitTime", Tag=2, Type=uint),
                    ])

            onOffControl: 'uint' = 0
            onTime: 'uint' = 0
            offWaitTime: 'uint' = 0


    class Attributes:
        @dataclass
        class OnOff(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=bool)

            value: 'bool' = False

        @dataclass
        class GlobalSceneControl(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x00004000

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.Optional[bool])

            value: 'typing.Optional[bool]' = None

        @dataclass
        class OnTime(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x00004001

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.Optional[uint])

            value: 'typing.Optional[uint]' = None

        @dataclass
        class OffWaitTime(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x00004002

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.Optional[uint])

            value: 'typing.Optional[uint]' = None

        @dataclass
        class StartUpOnOff(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x00004003

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.Union[None, Nullable, OnOff.Enums.OnOffStartUpOnOff])

            value: 'typing.Union[None, Nullable, OnOff.Enums.OnOffStartUpOnOff]' = None

        @dataclass
        class GeneratedCommandList(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000FFF8

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.List[uint])

            value: 'typing.List[uint]' = field(default_factory=lambda: [])

        @dataclass
        class AcceptedCommandList(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000FFF9

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.List[uint])

            value: 'typing.List[uint]' = field(default_factory=lambda: [])

        @dataclass
        class AttributeList(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000FFFB

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.List[uint])

            value: 'typing.List[uint]' = field(default_factory=lambda: [])

        @dataclass
        class FeatureMap(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000FFFC

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=typing.Optional[uint])

            value: 'typing.Optional[uint]' = None

        @dataclass
        class ClusterRevision(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0006

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000FFFD

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=uint)

            value: 'uint' = 0

