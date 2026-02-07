from src.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import sixteen_bit_signed_decimal_to_binary_array_no_print_statements
from src.decimal_to_binary.eight_bit.eight_bit_unsigned_decimal_to_binary_array import eight_bit_unsigned_decimal_to_binary_array_no_print_statements,eight_bit_unsigned_decimal_to_binary_array
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_signed_decimal_to_binary import thirty_two_bit_signed_decimal_to_binary_array_no_print_statements
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements,thirty_two_bit_unsigned_decimal_to_binary_array

def old_zero_extend_intro():
    print("zero_extend_intro")
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=8,to_size=16)))
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=16,to_size=32)))
    print("an issue with this is that you can't see this on the python front. \n so i would have to implment my decimal to binary bullshit on C for this to work good. which i could do if i had more time. I DON\'t")
    print(0xABCDEF30)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=0xABCDEF30))
    print(0xABCD0030)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=0xABCD0030))
    print()
    print(0xABCDEF30)
    print(0x00000030)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=0xABCDEF30))
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=0x00000030))

def new_zero_extend_intro():
    print("new_zero_extend_intro")
    print("test 1")
    #intended output = 2882338864
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2882400048,from_size=8,to_size=16)) )
    print()
    print("test 2")
    #intended output = 48
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2882400048,from_size=8,to_size=32)) )

def zero_extend_help(value, from_size, to_size):
    """
    typedef enum {
        ONE_BYTE    = 8,
        TWO_BYTES   = 16,
        FOUR_BYTES  = 32,
    } data_size_t;
    """

    """
    1. make a bitmask with the data_size_t vars
    2. make the value binary literal's range, based off of that bitmask, 0
        a. use ^ i think.
    3. spit out the binary literal, that 0ing causes.
   """

    """ make bitmask """
    # same as 0x11111111 <- 8 ones
    #                        0b1111'1111'1111'1111'1111'1111'1111'1111;
    four_byte_bit_mask_component_one = 0b11111111111111111111111111111111
    four_byte_bit_mask_component_two = 0b11111111111111111111111111111111
    four_byte_bit_mask_component_one = four_byte_bit_mask_component_one >> to_size
    four_byte_bit_mask_component_two = four_byte_bit_mask_component_two << from_size

    print("\tfour_byte_bit_mask_component_one")
    print("\t\t",thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(four_byte_bit_mask_component_one))
    print("\tfour_byte_bit_mask_component_two")
    print("\t\t",thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(four_byte_bit_mask_component_two))
    four_byte_bit_mask_full = four_byte_bit_mask_component_one & four_byte_bit_mask_component_two

    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=four_byte_bit_mask_full))
    print(thirty_two_bit_signed_decimal_to_binary_array_no_print_statements(decimal=~four_byte_bit_mask_full))
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=value))
    print()
    """ collide value binary literal, with bit mask """

    return value & ~four_byte_bit_mask_full

if __name__ == "__main__":
    new_zero_extend_intro()
