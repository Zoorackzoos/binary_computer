import math

from src.finished.decimal_to_binary.eight_bit.eight_bit_unsigned_decimal_to_binary_array import eight_bit_unsigned_decimal_to_binary_array_no_print_statements


def intro_exponentiate():
    print("binary difference between a number and a number at a exponent")
    print(eight_bit_unsigned_decimal_to_binary_array_no_print_statements(math.pow(2, 0)))
    print(eight_bit_unsigned_decimal_to_binary_array_no_print_statements(math.pow(2, 1)))
    print(eight_bit_unsigned_decimal_to_binary_array_no_print_statements(math.pow(2, 2)))
    print("eh fuck me then. :-/ it's << exponent_var. in a way ")
    print(2 >> 1, " versus ", math.pow(2, 0))
    print(2 << 1-1, " versus ", math.pow(2, 1))
    print(2 << 2-1, " versus ", math.pow(2, 2))
    print(2 << 3-1, " versus ", math.pow(2, 3))
    print()
    print(prototype_exponentiate(0))
    print(prototype_exponentiate(1))
    print(prototype_exponentiate(2))
    print(prototype_exponentiate(10))

def prototype_exponentiate(exponent):
    # 0 isn't allowed. so that edge case goes out the window
    # 32 isalso not allowed. though that doesn't matter in our prototype.
    return 1 << exponent

if __name__ == "__main__":
    intro_exponentiate()