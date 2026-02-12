import math

from src.finished.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_number_to_binary_array_no_print_statements

def intro_lg():
    print("testing for what the hell lg wants")
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(8))
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(math.log2(8)))
    print()
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(16))
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(math.log2(16)))
    print()
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(32))
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(math.log2(32)))
    print()
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(64))
    print(thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(math.log2(64)))
    print("there's no strict easy pattern here unless you have some mutned ass algorithm that checks bits like an array. and we can't do that.")
    print()
    """
    print("32 possible cases.... ????")
    for i in range(32):
        print("\t",math.pow(2, i))
    print("all that shit.")
    """
    print("compare some values")

    for i in range(32):
        print(prototype_lg(math.pow(2,i)), " == ", math.log2(math.pow(2,i)),"<--", math.pow(2,i), " --> \n\t\t\t\t\t\t\t\t\t\t", thirty_two_bit_unsigned_number_to_binary_array_no_print_statements(
            number=math.pow(2, i)))

"""
/**
 * Determines the base-two logarithm of an integer that is a power of two.
 * foo == exponentiate(bar) <--> bar == lg(foo). The argument must be a positive power of two.
 * @param power_of_two the value whose logarithm will be determined
 * @return base-2 logarithm of the argument
 */
 """
def prototype_lg(power_of_two):
    """
    https://www.reddit.com/r/jerma985/comments/rz9uky/heartwarming_jerma_hears_sound_again_after_30/

    :param power_of_two: this is a decimal number
    :return: the log2 of the decimal number
    """
    match power_of_two:
        case 1:
            return 0
        case 2:
            return 1
        case 4:
            return 2
        case 8:
            return 3
        case 16:
            return 4
        case 32:
            return 5
        case 64:
            return 6
        case 128:
            return 7
        case 256:
            return 8
        case 512:
            return 9
        case 1024:
            return 10
        case 2048:
            return 11
        case 4096:
            return 12
        case 8192:
            return 13
        case 16384:
            return 14
        case 32768:
            return 15
        case 65536:
            return 16
        case 131072:
            return 17
        case 262144:
            return 18
        case 524288:
            return 19
        case 1048576:
            return 20
        case 2097152:
            return 21
        case 4194304:
            return 22
        case 8388608:
            return 23
        case 16777216:
            return 24
        case 33554432:
            return 25
        case 67108864:
            return 26
        case 134217728:
            return 27
        case 268435456:
            return 28
        case 536870912:
            return 29
        case 1073741824:
            return 30
        case 2147483648:
            return 31
    return 0xFFFFFFFF


if __name__ == "__main__":
    intro_lg()