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
    def __init__(self, value=0, size=16, base="int"):
        if type(size) is not int:
            raise TypeError("Size must be int")

        self.__size = size
        self.__value = None
        self.set_value(value, base)

    # Comparison operators:
    # Each operator compares the value to an integer representation of another object
    def __lt__(self, other): return self.int() < int(other)

    def __le__(self, other): return self.int() <= int(other)

    def __eq__(self, other): return self.int() == int(other)

    def __ne__(self, other): return self.int() != int(other)

    def __ge__(self, other): return self.int() >= int(other)

    def __gt__(self, other): return self.int() > int(other)

    # Arithmetic operators:
    # Each operator performs an arithmetic operation on an integer representation of another object (if applicable)
    # and returns a new BitValue object (or self if an "in-place" version)
    def __abs__(self):
        value = self.__value if self[0] == '0' else -self.__value
        return BitValue(value, self.__size)

    def __neg__(self): return BitValue(-self.int(), self.__size)

    def __pos__(self): return BitValue(self.int(), self.__size)

    def __add__(self, other): return BitValue(self.int() + int(other), size=self.__size)

    def __sub__(self, other): return BitValue(self.int() - int(other), size=self.__size)

    def __mul__(self, other): return BitValue(self.int() * int(other), size=self.__size)

    def __mod__(self, other): return BitValue(self.int() % int(other), size=self.__size)

    def __div__(self, other): return BitValue(self.int() / int(other), size=self.__size)

    def __floordiv__(self, other): return BitValue(self.int() // int(other), size=self.__size)

    def __pow__(self, other):
        if int(other) < 0:
            raise ValueError("Exponent must be a positive integer")
        return BitValue(self.int() ** int(other), size=self.__size)

    # Bitwise operators:
    # Each operator performs a bitwise operation on an integer representation of another object (if applicable)
    # and returns a new BitValue object (or self if an "in-place" version)
    def __inv__(self): return BitValue(~self.__value, size=self.__size)

    def __and__(self, other): return BitValue(self.__value & int(other), size=self.__size)

    def __iand__(self, other):
        self.__value &= int(other)
        return self

    def __or__(self, other): return BitValue(self.__value | int(other), size=self.__size)

    def __ior__(self, other):
        self.__value |= int(other)
        return self

    def __xor__(self, other): return BitValue(self.__value ^ int(other), size=self.__size)

    def __ixor__(self, other):
        self.__value ^= int(other)
        return self

    def __lshift__(self, other): return BitValue(self.__value << other, size=self.__size)

    def __ilshift__(self, other):
        self.__value <<= other
        return self

    def __rshift__(self, other): return BitValue(self.__value >> other, size=self.__size)

    def __irshift__(self, other):
        self.__value >>= other
        return self

    # Check if value is zero for boolean expressions
    def __nonzero__(self): return self.__value != 0

    # Conversions:
    def __str__(self): return format(self.__value, "0" + str(self.__size) + "b")[-self.__size:]

    def __int__(self): return self.__value if self[0] == '0' else int(~self + 1) * -1

    def __hex__(self):
        size = int(self.get_size("hex"))
        return format(self.__value, "0" + str(size) + "x")[-size:].upper()

    # Getters:
    def __getitem__(self, key): return self.__str__()[key]

    def get_value(self): return self.__value

    def get_size(self, base="bin"):
        size_modifier = int(self.__info[base]["size_modifier"])
        # Do a ceiling division by the modifier for cases in which the number of bits isn't a whole multiple of
        # the target base
        # Example: 10 bits is a 3-digit hex number, not 2
        return ((self.__size - 1) / size_modifier) + 1

    # Setters:
    def __setitem__(self, key, value):
        start, stop, step = key.indices(self.__size) if type(key) is slice else (key, key + 1, 1)
        # Check equality of the size to avoid size changes
        if stop - start != len(value):
            raise ValueError("'" + str(value) + "' has a different length than the range given")

        new_value = list(self.bin())
        new_value[key] = value
        self.set_value("".join(new_value), base="bin")

    def set_value(self, value, base="int"):
        try:
            # Support base by name and as int value
            base = base if type(base) is int else int(self.__info[base]["base"])
            # Convert the value to a base-10 int for cases in which an int is given with a different base or
            # a string is given
            value = int(str(value), base)
            # Truncate the number according to the number of bits used
            self.__value = value % (2 ** self.__size)
        except KeyError as key_error:
            raise ValueError("'" + str(key_error.message) + "' is not a supported base")

    def set_size(self, size):
        if type(size) is not int:
            raise TypeError("Size must be int")
        if size < 1:
            raise ValueError("Size can't be smaller than 1")

        # Truncate the number according to the number of bits used if the new size is smaller
        if size < self.__size:
            self.__value = self.__value % (2 ** size)
        self.__size = size

    # Aliases:
    __invert__ = __inv__
    __bool__ = __nonzero__
    __len__ = get_size

    bin = __str__
    int = __int__
    hex = __hex__
