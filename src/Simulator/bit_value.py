#!/usr/bin/python
"""
bit_value.py

Created by Yuval Tzur on 08/12/2015.
"""


class BitValue:
    """ This class represents an integer value with the ability to manipulate it as a collection of bits"""

    # The info member holds a dictionary of commonly used configurations of different numerical bases
    __info = {"bin": {"base": 2,  "size_modifier": 1},
              "int": {"base": 10, "size_modifier": 1},
              "hex": {"base": 16, "size_modifier": 4}}
    __info["dec"] = __info["int"]

    # Each object has a size member and a value member
    # 'size' is the number of bits used
    # 'value' is an integer value that will be converted to a string for other numerical bases
    def __init__(self, value=0, size=16, base="bin"):
        if type(size) is not int:
            raise TypeError("Size must be int")

        self.__size = size
        self.__value = None
        self.set_value(value, base)

    # Comparison operators:
    # Each operator compares the value to an integer representation of another object
    def __lt__(self, other): return self.__value < int(other)

    def __le__(self, other): return self.__value <= int(other)

    def __eq__(self, other): return self.__value == int(other)

    def __ne__(self, other): return self.__value != int(other)

    def __ge__(self, other): return self.__value >= int(other)

    def __gt__(self, other): return self.__value > int(other)

    # Arithmetic operators:
    # Each operator performs an arithmetic operation on an integer representation of another object (if applicable)
    # and returns a new BitValue object (or self if an "in-place" version)
    def __abs__(self): return BitValue(abs(self.__value))

    def __neg__(self): return BitValue(-self.__value)

    def __pos__(self): return BitValue(+self.__value)

    def __add__(self, other): return BitValue(self.__value + int(other))

    def __iadd__(self, other):
        self.__value += int(other)
        return self

    def __sub__(self, other): return BitValue(self.__value - int(other))

    def __isub__(self, other):
        self.__value -= int(other)
        return self

    def __mul__(self, other): return BitValue(self.__value * int(other))

    def __imul__(self, other):
        self.__value *= int(other)
        return self

    def __mod__(self, other): return BitValue(self.__value % int(other))

    def __imod__(self, other):
        self.__value %= int(other)
        return self

    def __div__(self, other): return BitValue(self.__value / int(other))

    def __idiv__(self, other):
        self.__value /= int(other)
        return self

    def __floordiv__(self, other): return BitValue(self.__value // int(other))

    def __ifloordiv__(self, other):
        self.__value //= int(other)
        return self

    def __pow__(self, other): return BitValue(self.__value ** int(other))

    def __ipow__(self, other):
        self.__value **= int(other)
        return self

    # Bitwise operators:
    # Each operator performs a bitwise operation on an integer representation of another object (if applicable)
    # and returns a new BitValue object (or self if an "in-place" version)
    def __inv__(self): return BitValue(~self.__value)

    def __and__(self, other): return BitValue(self.__value & int(other))

    def __iand__(self, other):
        self.__value &= int(other)
        return self

    def __or__(self, other): return BitValue(self.__value | int(other))

    def __ior__(self, other):
        self.__value |= int(other)
        return self

    def __xor__(self, other): return BitValue(self.__value ^ int(other))

    def __ixor__(self, other):
        self.__value ^= int(other)
        return self

    def __lshift__(self, other): return BitValue(self.__value << other)

    def __ilshift__(self, other):
        self.__value <<= other
        return self

    def __rshift__(self, other): return BitValue(self.__value >> other)

    def __irshift__(self, other):
        self.__value >>= other
        return self

    # Check if value is zero for boolean expressions
    def __nonzero__(self): return self.__value != 0

    # Conversions:
    def __str__(self): return format(self.__value, "0" + str(self.__size) + "b")[-self.__size:]

    def __int__(self): return self.__value

    def __hex__(self):
        size = int(self.get_size("hex"))
        return format(self.__value, "0" + str(size) + "x")[-size:].upper()

    # Getters:
    def __getitem__(self, key): return self.__str__()[key]

    def get_value(self): return self.__value

    def get_size(self, base="bin"):
        size_modifier = int(self.__info[base]["size_modifier"])
        return (self.__size / size_modifier) + (self.__size % size_modifier != 0)

    # Setters:
    def __setitem__(self, key, value):
        start, stop, step = key.indices(self.__size) if type(key) is slice else (key, key + 1, 1)
        if stop - start != len(value):
            raise ValueError("'" + str(value) + "' has a different length than the range given")

        new_value = list(self.bin())
        new_value[key] = value
        self.set_value("".join(new_value), base="bin")

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

    # Aliases:
    __invert__ = __inv__
    __bool__ = __nonzero__
    __len__ = get_size

    bin = __str__
    int = __int__
    hex = __hex__
