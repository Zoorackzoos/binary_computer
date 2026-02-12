from src.finished.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import \
    thirty_two_bit_unsigned_number_to_binary_array_no_print_statements

if __name__ == "__main__":
    print("program started")

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
    #whateve rman. nothing ever happens

    print("program ended")