#!/usr/bin/python
"""
value.py

Created by Yuval Tzur on 08/12/2015.
"""


class Value:

    def __init__(self, value=0, size=16, base="bin"):
        self.__value = value
        self.__base = base
        self.__info = {"bin": {"base": 2, "get": self.bin, "size": size},
                       "int": {"base": 10, "get": self.int},
                       "hex": {"base": 16, "get": self.hex, "size": size / 4}}

    def __str__(self):
        return str(self.get())

    def __int__(self):
        return self.int()

    def __hex__(self):
        return self.hex()

    def __getitem__(self, item):
        return self.__str__()[item]

    def get(self):
        return self.__info[self.__base]["get"]()

    def set(self, value, base="bin"):
        value = value if type(value) is int else int(value, int(self.__info[base]["base"]))
        try:
            self.__value = value % 2**int(self.__info["bin"]["size"])
        except KeyError as key_error:
            value_error = ValueError("'" + key_error.message + "' is not a supported base")
            raise value_error

    def bin(self):
        size = int(self.__info["bin"]["size"])
        return format(self.__value, "0" + str(size) + "b")[-size:]

    def int(self):
        return self.__value

    def hex(self):
        size = int(self.__info["hex"]["size"])
        return format(self.__value, "0" + str(size) + "x")[-size:].upper()
