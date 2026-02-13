"""
thirty_two_bit_float_to_integer.py
"""
import struct
from src.finished.A_universal_functions.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import *

def thirty_two_bit_float_to_integer_A(integer):
    """
    Reinterprets a 32-bit integer's bits as an IEEE-754 float.
    """
    return struct.unpack('!f', struct.pack('!I', integer))[0]

def thirty_two_bit_float_to_integer_B(integer):
    sign = (integer >> 31) & 1
    exponent = (integer >> 23) & 0xFF
    fraction = integer & 0x7FFFFF

    if exponent == 0:
        mantissa = fraction / (1 << 23)
        value = mantissa * (2 ** (-126))
    else:
        mantissa = 1 + fraction / (1 << 23)
        value = mantissa * (2 ** (exponent - 127))

    return -value if sign else value

def test1():
    value = 0x000571cc
    # 5.000001076526666e-40
    print(thirty_two_bit_float_to_integer_A(value))
    # 5.000001076526666e-40
    print(thirty_two_bit_float_to_integer_B(value))
    # [0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 1, 0, 1, ' ', 0, 1, 1, 1, ' ', 0, 0, 0, 1, ' ', 1, 1, 0, 0, ' ', 1, 1, 0, 0]
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value))

def test_encode_12_375_examination():
    value1 = 1095106560
    print("expected: ",value1)
    print("\t",thirty_two_bit_float_to_integer_A(value1))
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value1))
    value2 = 4587523
    print("got: ",value2)
    print("\t",thirty_two_bit_float_to_integer_A(value2))
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value2))

if __name__ == "__main__":
    test_encode_12_375_examination()
