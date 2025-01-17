# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


class Speech2TextProcessor(metaclass=DummyObject):
    _backends = ["sentencepiece", "speech"]

    def __init__(self, *args, **kwargs):
        print('%s init', self.__classs__.__name__)
        requires_backends(self, ["sentencepiece", "speech"])
