import math

from src.finished.A_universal_functions.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import \
    thirty_two_bit_unsigned_number_to_binary_array_no_print_statements



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
    pass