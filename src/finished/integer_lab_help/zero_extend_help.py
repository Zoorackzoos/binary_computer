from src.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import sixteen_bit_signed_decimal_to_binary_array_no_print_statements
from src.decimal_to_binary.eight_bit.eight_bit_unsigned_decimal_to_binary_array import eight_bit_unsigned_decimal_to_binary_array_no_print_statements,eight_bit_unsigned_decimal_to_binary_array
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_signed_decimal_to_binary import thirty_two_bit_signed_decimal_to_binary_array_no_print_statements
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements,thirty_two_bit_unsigned_decimal_to_binary_array

def zero_extend_intro():
    print("zero_extend_intro")
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=8,to_size=16)))
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=16,to_size=32)))
    print("an issue with this is that you can't see this on the python front. \n so i would have to implment my decimal to binary bullshit on C for this to work good. which i could do if i had more time. I DON\'t")

def zero_extend_help(value, from_size, to_size):
    """
    typedef
    enum
    {
        ONE_BYTE = 8,
        TWO_BYTES = 16,
        FOUR_BYTES = 32,
    } data_size_t;
    """
    if from_size == 8:
        return value & 0xFF
    elif from_size == 16:
        return value & 0xFFFF
    else:
        return value

if __name__ == "__main__":
    zero_extend_intro()
