from src.finished.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import *
from src.finished.decimal_to_binary.eight_bit.eight_bit_unsigned_decimal_to_binary_array import *

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
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=bitmask_of_exponent_field))
    bitmask_of_exponent_field_bit_shifted = get_exponent(Ob=bitmask_of_exponent_field)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=bitmask_of_exponent_field_bit_shifted))

def get_exponent(Ob):
    return Ob >> (8+8+4+3)

if __name__ == "__main__":
    get_exponent_brief()