import math

from src.finished.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import \
    thirty_two_bit_unsigned_number_to_binary_array_no_print_statements

# SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
IEEE_754_matrix = \
    ["S","E","E","E"," ","E","E","E","E"," ","E","M","M","M"," ","M","M","M","M"," ","M","M","M","M"," ","M","M","M","M"," ","M","M","M","M"," ","M","M","M","M"]

def stringify_matrix(matrix):
    stringified_matrix = []
    for element in matrix:
        stringified_matrix.append(str(element))
    return stringified_matrix

def get_bias_from_IEEE_exponent_bit_emount(bits):
    """
    bias = 2 ^ (k - 1) − 1
        k = bits in the exponent field
            not the fucking bit rate. like 8 16 32 or 64

    single precision = 8 bits in exponent
    double precision = 11 bits in exponent
    half precision = 5 bits in exponent
    quad precision = 15 bits in exponent
    """
    return math.pow(2, bits - 1) - 1

def get_bias_from_IEEE_exponent_bit_emount_without_math_class(bits):
    return (1 << (bits - 1)) - 1

if __name__ == "__main__":
    print(get_bias_from_IEEE_exponent_bit_emount(8))
    print(get_bias_from_IEEE_exponent_bit_emount_without_math_class(8))
    print(0x000571cc)
    print(0x000571cc - get_bias_from_IEEE_exponent_bit_emount_without_math_class(8))
    print(IEEE_754_matrix)
    print(stringify_matrix(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(0x000571cc)))
    """
    [0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 1, 0, 1, ' ', 0, 1, 1, 1, ' ', 0, 0, 0, 1, ' ', 1, 1, 0, 0, ' ', 1, 1, 0, 0]
    """