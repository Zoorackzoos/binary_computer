import math

from src.finished.decimal_to_eight_bit_binary_array import decimal_to_eight_bit_binary_array_no_print_statements, decimal_to_eight_bit_binary_array

def intro_exponentiate():
    print("binary difference between a number and a number at a exponent")
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.pow(2, 0)))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.pow(2, 1)))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.pow(2, 2)))
    print("eh fuck me then. :-/ it's << exponent_var. in a way ")
    print(2 >> 1, " versus ", math.pow(2, 0))
    print(2 << 1-1, " versus ", math.pow(2, 1))
    print(2 << 2-1, " versus ", math.pow(2, 2))
    print()
    print(prototype_exponentiate(0))
    print(prototype_exponentiate(1))
    print(prototype_exponentiate(2))

def prototype_exponentiate(exponent):
    # 0 isn't allowed. so that edge case goes out the window
    # 32 isalso not allowed. though that doesn't matter in our prototype.
    return 2 << exponent


def intro_lg():
    print("testing for what the hell lg wants")
    print(decimal_to_eight_bit_binary_array_no_print_statements(8))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.log2(8)))
    print()
    print(decimal_to_eight_bit_binary_array_no_print_statements(16))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.log2(16)))
    print()
    print(decimal_to_eight_bit_binary_array_no_print_statements(32))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.log2(32)))
    print()
    print(decimal_to_eight_bit_binary_array_no_print_statements(64))
    print(decimal_to_eight_bit_binary_array_no_print_statements(math.log2(64)))
    print("comapre the binary literals with my super awesome funciton :DDDD")
    print((prototype_lg(8)))
    print((prototype_lg(16)))
    print((prototype_lg(32)))

"""
/**
 * Determines the base-two logarithm of an integer that is a power of two.
 * foo == exponentiate(bar) <--> bar == lg(foo). The argument must be a positive power of two.
 * @param power_of_two the value whose logarithm will be determined
 * @return base-2 logarithm of the argument
 */
 """
def prototype_lg(power_of_two):
    pass

if __name__ == "__main__":
    intro_exponentiate()