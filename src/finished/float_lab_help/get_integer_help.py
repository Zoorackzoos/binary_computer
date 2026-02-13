from src.finished.float_lab_help.thirty_two_bit_float_to_integer import *
from src.finished.A_universal_functions.thirty_two_bit.float.IEEE_754_header_array_and_stringify_matrix import stringify_matrix, IEEE_754_matrix

def bohn_lame_explantion():
    """

    :return: print statements explaining what bohn was yapping about on piazza. spoiler but it's shit
    """
    print("bohn_lame_explantion started")
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
    print("bit shift: \n\t bitmask_of_exponent_field >> 4")
    four_shifted_bitmask_of_exponent_field = bitmask_of_exponent_field >> 4
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(
        number=four_shifted_bitmask_of_exponent_field))
    # whateve rman. nothing ever happens

    print("bohn_lame_explantion ended")

def get_754_integer(bit_pattern: int) -> int:
    """
    Returns the implicit leading significand bit
    from a 32-bit IEEE-754 float stored as an int.

    :param bit_pattern: an integer. hex, binary literal, python integer. whatever
    :return the integer value for which will be multiplied by 10^expo
        integer * 10^expo
            that
    """

    # extract exponent (bits 30–23)
    exponent = (bit_pattern >> 23) & 0xFF

    # integer bit rule
    if exponent == 0:
        integer_bit = 0
    else:
        integer_bit = 1

    return integer_bit


def what_is_get_integer_frfr():
    """
    TEST(test_3f800000)
        ieee754_t value = 0x3f80'0000;
        uint8_t expected_integer = 1;
        uint32_t expected_fraction = 0b0000'0000'0000'0000'0000'000;
        int8_t expected_exponent = 0;
        ASSERT_FALSE(is_negative(value));
        ASSERT_EQUAL(expected_integer, get_754_integer(value));
        ASSERT_EQUAL(expected_fraction, get_754_fraction(value));
        ASSERT_EQUAL(expected_exponent, get_754_exponent(value));
    END_TEST

    TEST(test_encode_12_375)
        unnormal_t value = unnormal(.sign = 0, .integer = 99, .fraction = 0, .exponent = -3);
        ieee754_t expected_result = ((union float_converter){.reference_value = 12.375f}).bit_vector;
        ieee754_t actual_result = encode(value);
        ASSERT_EQUAL(expected_result, actual_result);
    END_TEST

    :return: print statements explaining what get_integer is supposed to do
    """
    print("what_is_get_integer_frfr started")
    print()
    test1_value = 0x3f800000
    print("test1_value as python integer = \n\t",test1_value)
    print("test1_value as binary = \n\t",IEEE_754_matrix,"\n\t",stringify_matrix( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=test1_value)) )
    print("test1_value as IEEE 754 float = \n\t",thirty_two_bit_float_to_integer_A(test1_value))
    print("this thing's exponent bits are 0111'1111 . in decimal that's 127.")
    print("\t127 - 127 (the bias) = 0 . that' snot allowed to happen because of IEEE rule apparently. so it's 1, not 0.")
    print("\t1")
    print("how get integer?")
    test1_integer_value = get_754_integer(test1_value)
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=test1_value))
    print("\tget_integer used")
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(test1_integer_value))
    print("\t\t",test1_integer_value)
    print("scientific notation of that:")
    print("\t1 * 10^0")
    print("\tAKA: 1")
    print()
    test2_value = 1095106560
    print("test2_value as python integer = \n\t",test2_value)
    print("test2_value as binary = \n\t",IEEE_754_matrix,"\n\t",stringify_matrix( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=test2_value)) )
    print("test2_value as IEEE 754 float = \n\t",thirty_two_bit_float_to_integer_A(test2_value))
    print("this thing's exponent bits are 1000'0010 . in decimal that's 130.")
    print("\t130 - 127")
    print("\t-3")
    print("\tthat's what our exponent answer should be.")
    print("how get integer?")
    test2_integer_value = get_754_integer(test2_value)
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(test2_value))
    print("\tget_integer used")
    print("\t",thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(test2_integer_value))
    print("\t\t",test2_integer_value)
    print("scientific notation of that:")
    print("\t99 * 10^-3")
    print()
    print("what_is_get_integer_frfr ended")

def what_is_get_integer_two():

    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(1095106560))

if __name__ == "__main__":
    what_is_get_integer_two()

"""
EXPECTED:   0x41460000
GOT:        0x00460082
EXPECTED:   1095106560
GOT:        4587650
EXPECTED:   01000001010001100000000000000000
GOT:        00000000010001100000000010000010

hex:            3f800000
IEEE header:    SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
binary:         0011'1111'1000'0000'0000'0000'0000'0000
decimal;        1065353216
expected int:   1 <- fuck idk man 
expected frac:  0b0000'0000'0000'0000'0000'000 <- just get it form the M in the binary
expected expo:  0 <- 127 - 127 <- exponent - bias
    1 * 10^0
    
hex:            3e800000
IEEE header:    SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
binary:         0011'1110'1000'0000'0000'0000'0000'0000
decimal;        1048576000
expected int:   1 <- fuck idk man 
expected frac:  0b0000'0000'0000'0000'0000'000
expected expo:  -2 <- 130 - 127 <- exponent - bias

----------------DECODE--------------------
hex:            41460000
IEEE header:    SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
binary:         0100'0001'0100'0110'0000'0000'0000'0000
decimal;        1095106560
float:          12.375
expected sign:  0
expected int:   1 <- 0x1
expected frac:  0x8c00'0000'0000'0000
expected expo:  3
--------------do this happy horseshit backwards---------------
--------------encode------------------
hex:            41460000
IEEE header:    SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
binary:         0100'0001'0100'0110'0000'0000'0000'0000
decimal;        1095106560
float:          12.375
expected sign:  0
expected int:   1 <- 0x1
expected frac:  0x8c00'0000'0000'0000
expected expo:  3

"""