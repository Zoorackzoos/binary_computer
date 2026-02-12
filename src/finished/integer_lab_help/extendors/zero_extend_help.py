from src.finished.decimal_to_binary.sixteen_bit.sixteen_bit_signed_decimal_to_binary import sixteen_bit_signed_decimal_to_binary_array_no_print_statements
from src.finished.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_number_to_binary_array_no_print_statements


def old_zero_extend_intro():
    print("zero_extend_intro")
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=8,to_size=16)))
    print(sixteen_bit_signed_decimal_to_binary_array_no_print_statements( zero_extend_help(value=2,from_size=16,to_size=32)))
    print("an issue with this is that you can't see this on the python front. \n so i would have to implment my decimal to binary bullshit on C for this to work good. which i could do if i had more time. I DON\'t")
    print(0xABCDEF30)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=0xABCDEF30))
    print(0xABCD0030)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=0xABCD0030))
    print()
    print(0xABCDEF30)
    print(0x00000030)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=0xABCDEF30))
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=0x00000030))

def new_zero_extend_intro():
    print("new_zero_extend_intro")
    print("test 1")
    #intended output = 2882338864
    test_1_output = zero_extend_help(value=2882400048,from_size=8,to_size=16)
    print(test_1_output)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(test_1_output))
    print()
    print("test 2")
    #intended output = 48
    test_2_output = zero_extend_help(value=2882400048,from_size=8,to_size=32)
    print(test_2_output)
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(test_2_output))


def zero_extend_help(value, from_size, to_size):
    # Create mask for bits [from_size, to_size) that need to be zeroed

    # Mask with 1s in positions [0, from_size)
    lower_mask = ~(0xFFFFFFFF << from_size) & 0xFFFFFFFF

    # Mask with 1s in positions [to_size, 32)
    if to_size >= 32: #YOU HAVE TO CHANTGE THIS TO equal(to_size >= 32) IN C BECUASE YOU CAN'T USE LOGICAL OPERATORS. how tf does this benefit me at all?
        upper_mask = 0
    else:
        upper_mask = 0xFFFFFFFF << to_size

    # Combine: keep lower bits and upper bits
    keep_mask = lower_mask | upper_mask

    print("\tlower_mask")
    print("\t\t", thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(lower_mask))
    print("\tupper_mask")
    print("\t\t", thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(upper_mask))
    print("\tkeep_mask")
    print("\t\t", thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(keep_mask))
    print("\tvalue")
    print("\t\t", thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value))
    print()

    return value & keep_mask

if __name__ == "__main__":
    new_zero_extend_intro()
