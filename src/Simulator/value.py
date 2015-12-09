#!/usr/bin/python
"""
value.py

Created by Yuval Tzur on 08/12/2015.
"""

import pprint


class Value:

    def __init__(self, value=0, size=16, base="bin"):
        self.__info = {"bin": {"base": 2, "size_modifier": 1, "get": self.bin},
                       "int": {"base": 10, "size_modifier": 1,  "get": self.int},
                       "hex": {"base": 16, "size_modifier": 4,  "get": self.hex}}
        self.set_base(base)
        self.set_size(size)
        self.set_value(value, base)

    __lt__ = lambda self, x: self.__value < int(x)
    __le__ = lambda self, x: self.__value <= int(x)
    __eq__ = lambda self, x: self.__value == int(x)
    __ne__ = lambda self, x: self.__value != int(x)
    __ge__ = lambda self, x: self.__value >= int(x)
    __gt__ = lambda self, x: self.__value > int(x)

    __nonzero__ = lambda self: self.__value != 0
    __bool__ = __nonzero__

    get = lambda self: self.__info[self.__base]["get"]()
    __str__ = lambda self: str(self.get())
    __getitem__ = lambda self, key: self.__str__()[key]

    bin = lambda self: format(self.__value, "0" + str(self.__size) + "b")[-self.__size:]
    int = lambda self: self.__value
    __int__ = int
    hex = lambda self: format(self.__value, "0" + str(self.get_size("hex")) + "x")[-self.get_size("hex"):].upper()
    __hex__ = hex

    __abs__ = lambda self: Value(abs(self.__value))
    __neg__ = lambda self: Value(-self.__value)
    __pos__ = lambda self: Value(+self.__value)
    __add__ = lambda self, x: Value(self.__value + int(x))
    __sub__ = lambda self, x: Value(self.__value - int(x))
    __mul__ = lambda self, x: Value(self.__value * int(x))
    __mod__ = lambda self, x: Value(self.__value % int(x))
    __div__ = lambda self, x: Value(self.__value / int(x))
    __floordiv__ = lambda self, x: Value(self.__value // int(x))
    __pow__ = lambda self, x: Value(self.__value ** int(x))

    __inv__ = lambda self: Value(~self.__value)
    __invert__ = __inv__
    __and__ = lambda self, x: Value(self.__value & int(x))
    __or__ = lambda self, x: Value(self.__value | int(x))
    __xor__ = lambda self, x: Value(self.__value ^ int(x))
    __lshift__ = lambda self, x: Value(self.__value << x)
    __rshift__ = lambda self, x: Value(self.__value >> x)

    get_value = lambda self: self.__value
    get_base = lambda self: self.__base
    
    def __setitem__(self, key, value):
        new_value = list(self.get())
        new_value[key] = value
        self.set_value("".join(new_value), base = self.__base)

    def set_value(self, value, base=None):
        base = self.__base if not base else base
        value = value if type(value) is int else int(value, int(self.__info[base]["base"]))
        try:
            self.__value = value % (2 ** self.__size)
        except KeyError as key_error:
            value_error = ValueError("'" + key_error.message + "' is not a supported base")
            raise value_error
    
    set = set_value

    def set_base(self, base):
        if base in self.__info:
            self.__base = base
        else:
            value_error = ValueError("'" + base + "' is not a supported base")
            raise value_error

    def get_size(self, base=None):
        base = self.__base if not base else base
        return  (self.__size / self.__info[base]["size_modifier"]) + (self.__size % self.__info[base]["size_modifier"] != 0)

    __len__ = get_size

    def set_size(self, size, base="bin"):
        if type(size) is not int:
            raise TypeError("Size must be int")

        self.__size = size * self.__info[base]["size_modifier"]

    def details(self):
        print "Value: " + str(self.__value)
        print "Base: " + self.__base
        print "Size: " + str(self.__size)
        print "Binary: " + self.bin()
        print "Decimal: " + str(self.int())
        print "Hexadecimal: " + self.hex()
        print "Info:"
        pprint.pprint(self.__info)
