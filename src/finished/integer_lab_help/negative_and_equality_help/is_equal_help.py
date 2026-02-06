from src.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import \
    sixteen_bit_signed_decimal_to_binary_array_no_print_statements


def intro_is_equal():
    print("find if 2 integers are qual based on their \"binary\" vector. whatever that means. just use bitwise operations like a true gamer")
    print("5 == 5 -> ",5 == 5, is_equal_help(value1=5, value2=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))

    print("5 == -5 -> ",5 == -5, is_equal_help(value1=5, value2=-5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-5))

    print("5 == 10 -> ",5 == 10, is_equal_help(value1=5, value2=10))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=10))

    print("5 == 7 -> ", 5 == 7, is_equal_help(value1=5, value2=7))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=7))
    print()
    print("i suppose i could bit shift and compare each bit 16 times. that's dumb though.")

"""
Determines whether two values are equal.
Two values are considered equal if their bit vectors are identical.

this is the same variable type as the one that's signed. so i'm going to assume it's signed.

@param value1 the first value for the comparison
@param value2 the second value for the comparison
@return 1 if the two arguments are equal; 0 otherwise
"""
def is_equal_help(value1, value2):
    return (value1 & value2) != 0

if __name__ == "__main__":
    intro_is_equal()