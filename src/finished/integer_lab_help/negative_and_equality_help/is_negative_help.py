from src.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import \
    sixteen_bit_signed_decimal_to_binary_array_no_print_statements


def intro_is_negative():
    print("determine if something is negative. i've been told the binary literal has to be signed, and then the biggest binary slot is the negative one. however idk how that works in C.")
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements(5))
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements(0))
    print(0x8000)
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements(32768))


def is_negative_prototype(value):
    """

    :param value: a positive integer within 16 bits. fml. just pick one bro.
    :return: boolean value if the value is negative
    """
    is_negative_bool = False

    return is_negative_bool

if __name__ == "__main__":
    intro_is_negative()