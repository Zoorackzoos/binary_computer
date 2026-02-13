from src.finished.float_lab_help.thirty_two_bit_float_to_integer import *
from src.finished.A_universal_functions.thirty_two_bit.float.get_bias import get_bias_from_IEEE_exponent_bit_emount_without_math_class,get_bias_from_IEEE_exponent_bit_emount
from src.finished.A_universal_functions.thirty_two_bit.float.IEEE_754_header_array_and_stringify_matrix import IEEE_754_matrix, stringify_matrix

def get_exponent_brief():
    print("get_exponent_brief")
    """
        IEEE 754

        S -> 1 = sign
        E -> 8 = exponent
        M -> 23 = martissa <- or fraction. if i set it as F it looks like E.
            just remember that by knowing people experience hernias at thsi age the most

        SEEE    EEEE    EMMM    MMMM    MMMM    MMMM    MMMM    MMMM
        ????    ????    ????    ????    ????    ????    ????    ????
        """
    bitmask_of_exponent_field = 0b01111111100000000000000000000000
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=bitmask_of_exponent_field))

    bitmask_of_exponent_field_bit_shifted = get_exponent(Ob=bitmask_of_exponent_field)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(
        number=bitmask_of_exponent_field_bit_shifted))

    bitmask_of_exponent_field_bit_shifted_with_bias = get_exponent_with_bias(Ob=bitmask_of_exponent_field)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=bitmask_of_exponent_field_bit_shifted_with_bias))

def get_exponent(Ob):
    return (Ob >> 23) #- get_bias_from_IEEE_exponent_bit_emount(8)
def get_exponent_with_bias(Ob):
    return (Ob >> 23) - get_bias_from_IEEE_exponent_bit_emount_without_math_class(bits=8)

def fuck():
    print(-128)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(128))

if __name__ == "__main__":
    fuck()