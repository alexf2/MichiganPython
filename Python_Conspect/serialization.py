import math
import reprlib
from array import array


class Vector:
    typecode = 'd'

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)

        return cls(memv)
