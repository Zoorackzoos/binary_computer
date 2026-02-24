from src.finished.A_universal_functions.sixteen_bit.sixteen_bit_signed_decimal_to_binary import \
    sixteen_bit_signed_decimal_to_binary_array_no_print_statements
from src.finished.A_universal_functions.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_number_to_binary_array_no_print_statements,thirty_two_bit_unsigned_number_to_binary_array
from src.finished.A_universal_functions.thirty_two_bit.float.get_bias import get_bias_from_IEEE_exponent_bit_emount_without_math_class, get_bias_from_IEEE_exponent_bit_emount, thirty_two_bit_unsigned_number_to_binary_array_no_print_statements
from src.finished.A_universal_functions.thirty_two_bit.float.IEEE_754_header_array_and_stringify_matrix import IEEE_754_matrix



if __name__ == "__main__":
    print("main started")
    print( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=(0xEC02)) )
    print( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(number=(0xEC02 << 3)) )
    #[0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 0, 0, 0, ' ', 0, 1, 1, 1, ' ', 0, 1, 1, 0, ' ', 0, 0, 0, 0, ' ', 0, 0, 0, 1, ' ', 0, 0, 0, 0]
    print(0b00000000000001110110000000010000)
    print("main finished")