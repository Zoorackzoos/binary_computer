from src.finished.A_universal_functions.eight_bit.eight_bit_unsigned_decimal_to_binary_array import \
    eight_bit_unsigned_decimal_to_binary_array_no_print_statements
from src.finished.A_universal_functions.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_number_to_binary_array_no_print_statements,thirty_two_bit_unsigned_number_to_binary_array
from src.finished.A_universal_functions.thirty_two_bit.float.get_bias import get_bias_from_IEEE_exponent_bit_emount_without_math_class, get_bias_from_IEEE_exponent_bit_emount, thirty_two_bit_unsigned_number_to_binary_array_no_print_statements
from src.finished.A_universal_functions.thirty_two_bit.float.IEEE_754_header_array_and_stringify_matrix import IEEE_754_matrix
from src.finished.A_universal_functions.thirty_two_bit.stringify_matrix import stringify_matrix
from src.finished.A_universal_functions.thirty_two_bit.thirty_two_bit_value_header import thirty_two_bit_value_header

"""
ex:
    6               2.5
    1.10 x 2^2  *   1.01 x 2^1
    ->
    sign -> 0 ^ 0 -> 0
    ->
    exponent -> 1 + 2 -> 3
    ->
    fraction -> 1.10 x 1.01 = 1.1110
        ripple carry adder? isn't that just what + is?
    ->          
    result -> 1.111 x 2^3 <- 15 
"""
if __name__ == '__main__':
    value1 = 0x40A00000 #epxected
    value2 = 0x41000000 #got
    print(IEEE_754_matrix)
    print(stringify_matrix( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value1)) )
    print(stringify_matrix( thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(value2)) )
    print(stringify_matrix( eight_bit_unsigned_decimal_to_binary_array_no_print_statements(0b10000010)))
    print(0b10000010)



