#!/usr/bin/python
"""
Bitvalue.py

Created by Yuval Tzur on 08/12/2015.
"""

import pprint


class BitValue:

    __info = {"bin": {"base": 2, "size_modifier": 1, "get": bin},
                   "int": {"base": 10, "size_modifier": 1, "get": int},
                   "hex": {"base": 16, "size_modifier": 4, "get": hex}}

    def __init__(self, value=0, size=16, base="bin"):
        if type(size) is not int:
            raise TypeError("Size must be int")

        self.__size = size
        self.set_value(value, base)

    __lt__ = lambda self, x: self.__value < int(x)
    __le__ = lambda self, x: self.__value <= int(x)
    __eq__ = lambda self, x: self.__value == int(x)
    __ne__ = lambda self, x: self.__value != int(x)
    __ge__ = lambda self, x: self.__value >= int(x)
    __gt__ = lambda self, x: self.__value > int(x)

    __abs__ = lambda self: BitValue(abs(self.__value))
    __neg__ = lambda self: BitValue(-self.__value)
    __pos__ = lambda self: BitValue(+self.__value)
    __add__ = lambda self, x: BitValue(self.__value + int(x))
    __sub__ = lambda self, x: BitValue(self.__value - int(x))
    __mul__ = lambda self, x: BitValue(self.__value * int(x))
    __mod__ = lambda self, x: BitValue(self.__value % int(x))
    __div__ = lambda self, x: BitValue(self.__value / int(x))
    __floordiv__ = lambda self, x: BitValue(self.__value // int(x))
    __pow__ = lambda self, x: BitValue(self.__value ** int(x))

    __inv__ = lambda self: BitValue(~self.__value)
    __invert__ = __inv__
    __and__ = lambda self, x: BitValue(self.__value & int(x))
    __or__ = lambda self, x: BitValue(self.__value | int(x))
    __xor__ = lambda self, x: BitValue(self.__value ^ int(x))
    __lshift__ = lambda self, x: BitValue(self.__value << x)
    __rshift__ = lambda self, x: BitValue(self.__value >> x)

    __nonzero__ = lambda self: self.__value != 0
    __bool__ = __nonzero__

    __str__ = lambda self: format(self.__value, "0" + str(self.__size) + "b")[-self.__size:]
    __int__ = lambda self: self.__value
    __hex__ = lambda self: format(self.__value, "0" + str(self.get_size("hex")) + "x")[-self.get_size("hex"):].upper()
    __len__ = lambda self: self.__size
    
    __getitem__ = lambda self, key: self.__str__()[key]

    bin = __str__
    int = __int__
    hex = __hex__

    get_value = lambda self: self.__value
    get_size = lambda self, base="bin": (self.__size / self.__info[base]["size_modifier"]) + (self.__size % self.__info[base]["size_modifier"] != 0)

    def __setitem__(self, key, value):
        start, stop, step = key.indices(self.__size) if type(key) is slice else (key, key + 1, 1)
        if stop - start != len(value):
            raise ValueError("'" + str(value) + "' has a different length than the range given")

        new_value = list(self.bin())
        new_value[key] = value
        self.set_value("".join(new_value), base = "bin")

    def set_value(self, value, base="bin"):
        try:
            base = base if type(base) is int else int(self.__info[base]["base"])
            value = value if type(value) is int else int(value, base)
            self.__value = value % (2 ** self.__size)
        except KeyError as key_error:
            raise ValueError("'" + str(key_error.message) + "' is not a supported base")

    def set_size(self, size):
        if type(size) is not int:
            raise TypeError("Size must be int")
        if size < 1:
            raise ValueError("Size can't be smaller than 1")

        self.__size = size
        self.set_value(self.__value)

    def details(self):
        print "Value: " + str(self.__value)
        print "Size: " + str(self.__size)
        print "Binary: " + self.bin()
        print "Decimal: " + str(self.int())
        print "Hexadecimal: " + self.hex()
        print "Info:"
        pprint.pprint(self.__info)
