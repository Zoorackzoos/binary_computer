from src.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import \
    sixteen_bit_signed_decimal_to_binary_array_no_print_statements


def intro_is_negative():
    print("determine if something is negative. i've been told the binary literal has to be signed, and then the biggest binary slot is the negative one. however idk how that works in C.")
    print(is_negative_prototype(5), "<-- 5")
    print(is_negative_prototype(-5), "<-- -5")
    print("who's gonna argue with that?")


def is_negative_prototype(value):
    """
    technically i could just do returnarray[0] and see if it's equal to 1 or 0
    but that's not something i can do in C.

    1. make a bitmask for the greatest digit
    2. do:
        https://www.tutorialspoint.com/cprogramming/c_bitwise_operators.htm
        value | bit_mask -> value_versus_bit_mask_result
    3. if the result is different from value, then it's positive
        if the result is the same, then it's negative

    :param value: a positive integer within 16 bits. fml. just pick one bro.
    :return: boolean value if the value is negative
    """

    # if you're on 8 bit or 32 bit, change this to 7 or 31 respectively
    bit_count = 15
    # the greatest bit. all the way to the left. is 1. the rest are 0
    bit_mask = -1 << bit_count

    value_versus_bit_mask_result = value | bit_mask

    is_negative_bool = False
    if value == value_versus_bit_mask_result:
        is_negative_bool = True

    return is_negative_bool

if __name__ == "__main__":
    intro_is_negative()