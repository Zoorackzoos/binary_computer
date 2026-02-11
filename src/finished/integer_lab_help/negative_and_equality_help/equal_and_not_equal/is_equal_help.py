from src.finished.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import \
    sixteen_bit_signed_decimal_to_binary_array_no_print_statements


def intro_is_equal_peepee_poopoo_version():
    print("find if 2 integers are qual based on their \"binary\" vector. whatever that means. just use bitwise operations like a true gamer")
    print("5 == 5 -> ", 5 == 5, is_equal_help_peepee_poopoo_version(value1=5, value2=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))

    print("5 == -5 -> ", 5 == -5, is_equal_help_peepee_poopoo_version(value1=5, value2=-5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-5))

    print("5 == 10 -> ", 5 == 10, is_equal_help_peepee_poopoo_version(value1=5, value2=10))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=10))

    print("5 == 7 -> ", 5 == 7, is_equal_help_peepee_poopoo_version(value1=5, value2=7))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=7))

    print("16 == 16 -> ", 16 == 16, is_equal_help_peepee_poopoo_version(value1=16, value2=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))

    print("16 == -16 -> ", 16 == -16, is_equal_help_peepee_poopoo_version(value1=16, value2=-16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-16))
"""
Determines whether two values are equal.
Two values are considered equal if their bit vectors are identical.

this is the same variable type as the one that's signed. so i'm going to assume it's signed.

@param value1 the first value for the comparison
@param value2 the second value for the comparison
@return 1 if the two arguments are equal; 0 otherwise
"""
def is_equal_help_peepee_poopoo_version(value1, value2):

    # bit masks
    # 0000'0000'0000'0001
    bitmask_1 = 0x0001
    # 0000'0000'0000'0010
    bitmask_2 = 0x0002
    # 0000'0000'0000'0100
    bitmask_4 = 0x0004
    # 0000'0000'0000'1000
    bitmask_8 = 0x0008

    # 0000'0000'0001'0000
    bitmask_16 = 0x0010
    # 0000'0000'0010'0000
    bitmask_32 = 0x0020
    # 0000'0000'0100'0000
    bitmask_64 = 0x0040
    # 0000'0000'1000'0000
    bitmask_128 = 0x0080

    # 0000'0001'0000'0000
    bitmask_256 = 0x0100
    # 0000'0010'0000'0000
    bitmask_512 = 0x0200
    # 0000'0100'0000'0000
    bitmask_1024 = 0x0400
    # 0000'1000'0000'0000
    bitmask_2048 = 0x0800

    # 0001'0000'0000'0000
    bitmask_4096 = 0x1000
    # 0010'0000'0000'0000
    bitmask_8192 = 0x2000
    # 0100'0000'0000'0000
    bitmask_16384 = 0x4000
    # 1000'0000'0000'0000
    bitmask_32768 = 0x8000

    #collection of booleans
    bool_1 = ((value1 | bitmask_1) == value1) == ((value2 | bitmask_1) == value2)
    bool_2 = ((value1 | bitmask_2) == value1) == ((value2 | bitmask_2) == value2)
    bool_4 = ((value1 | bitmask_4) == value1) == ((value2 | bitmask_4) == value2)
    #print("((value1 | bitmask_4) == value1) == ((value2 | bitmask_4) == value2)")
    #print((value1 | bitmask_4), value1, (value2 | bitmask_4), value2)
    #print((value1 | bitmask_4) == value1, (value2 | bitmask_4) == value2)
    #print((value1 | bitmask_4) == value1 == (value2 | bitmask_4) == value2)
    #print(bool_4)
    bool_8 = ((value1 | bitmask_8) == value1) == ((value2 | bitmask_8) == value2)

    bool_16 = ((value1 | bitmask_16) == value1) == ((value2 | bitmask_16) == value2)
    bool_32 = ((value1 | bitmask_32) == value1) == ((value2 | bitmask_32) == value2)
    bool_64 = ((value1 | bitmask_64) == value1) == ((value2 | bitmask_64) == value2)
    bool_128 = ((value1 | bitmask_128) == value1) == ((value2 | bitmask_128) == value2)

    bool_256 = ((value1 | bitmask_256) == value1) == ((value2 | bitmask_256) == value2)
    bool_512 = ((value1 | bitmask_512) == value1) == ((value2 | bitmask_512) == value2)
    bool_1024 = ((value1 | bitmask_1024) == value1) == ((value2 | bitmask_1024) == value2)
    bool_2048 = ((value1 | bitmask_2048) == value1) == ((value2 | bitmask_2048) == value2)

    bool_4096 = ((value1 | bitmask_4096) == value1) == ((value2 | bitmask_4096) == value2)
    bool_8192 = ((value1 | bitmask_8192) == value1) == ((value2 | bitmask_8192) == value2)
    bool_16384 = ((value1 | bitmask_16384) == value1) == ((value2 | bitmask_16384) == value2)
    bool_32768 = ((value1 | bitmask_32768) == value1) == ((value2 | bitmask_32768) == value2)
    print("\t\t",bool_1,bool_2,bool_4,bool_8,bool_16,bool_32,bool_64,bool_128,bool_256,bool_512,bool_1024,bool_2048,bool_4096,bool_8192,bool_16384,bool_32768,bool_64)

    return (bool_1 == bool_2 ==
            bool_4 == bool_8 ==
            bool_16 == bool_32 ==
            bool_64 == bool_128 ==
            bool_256 == bool_512 ==
            bool_1024 == bool_2048 ==
            bool_4096 == bool_8192 ==
            bool_16384 == bool_32768)

def intro_is_equal_superior():
    print("find if 2 integers are qual based on their \"binary\" vector. whatever that means. just use bitwise operations like a true gamer")
    print("5 == 5 -> ", 5 == 5, is_equal_help_superior(value1=5, value2=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))

    print("5 == -5 -> ", 5 == -5, is_equal_help_superior(value1=5, value2=-5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-5))

    print("5 == 10 -> ", 5 == 10, is_equal_help_superior(value1=5, value2=10))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t",sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=10))

    print("5 == 7 -> ", 5 == 7, is_equal_help_superior(value1=5, value2=7))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=5))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=7))

    print("16 == 16 -> ", 16 == 16, is_equal_help_superior(value1=16, value2=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))

    print("16 == -16 -> ", 16 == -16, is_equal_help_superior(value1=16, value2=-16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=16))
    print("\t", sixteen_bit_signed_decimal_to_binary_array_no_print_statements(decimal=-16))

def is_equal_help_superior(value1, value2):
    #what a fool i am.
    return (value1 ^ value2) == 0

if __name__ == "__main__":
    intro_is_equal_superior()







