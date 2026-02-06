import math


def thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal):
    """
    LIMITATION / CONTEXT NOTE:
    --------------------------
    This function assumes a 32-bit two's complement representation.
    Negative values are first converted to their unsigned two's complement
    equivalent before bit extraction.

    Because the original unsigned algorithm works by subtracting powers of two,
    we MUST do this conversion up front. There is no way to "see" negative bits
    directly using subtraction alone.
    """

    # Enforce 32-bit signed range explicitly
    if decimal < -2147483648 or decimal > 2147483647:
        raise ValueError("Value out of 32-bit signed integer range")

    # If negative, convert to unsigned two's complement representation
    if decimal < 0:
        # two's complement: 2^32 - |decimal|
        decimal = math.pow(2, 32) + decimal
        # NOTE: decimal is now non-negative and fits the unsigned logic

    return_array = []
    four_bit_readability_counter = 0

    # 32 bits total → highest bit index is 31
    n = 31

    infinite_loop_counter = 0
    infinite_loop_counter_limit = 100

    while decimal >= 0 and n >= 0 and infinite_loop_counter < infinite_loop_counter_limit:

        if four_bit_readability_counter == 4:
            return_array.append(" ")
            four_bit_readability_counter = 0

        if (decimal - (math.pow(2, n))) >= 0:
            decimal = decimal - math.pow(2, n)
            return_array.append(1)
        else:
            return_array.append(0)

        n -= 1
        four_bit_readability_counter += 1
        infinite_loop_counter += 1

    return return_array

if __name__ == "__main__":
    print(thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-32))
    print(-1 + -1 + -2 + -4 + -8 + -16)
    print(thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-1))
    print(-1)
    print(thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-2147483647))
    print(-2147483647)
    print(thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-2147483648))
    print(-2147483648)