import math

def sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal):
    """
    derived from the thirty_two_bit one of this

    :param decimal: decimal
    :return: binary array representing a decimal.
    """

    # Enforce 16-bit signed range explicitly
    if decimal < -32768 or decimal > 32768:
        raise ValueError("Value out of 16-bit signed integer range")

    # If negative, convert to unsigned two's complement representation
    if decimal < 0:
        # two's complement: 2^16 - |decimal|
        decimal = math.pow(2, 16) + decimal
        # NOTE: decimal is now non-negative and fits the unsigned logic

    return_array = []
    four_bit_readability_counter = 0

    # 16 bits total → highest bit index is 15
    n = 15

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
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-1))
    print(-1)