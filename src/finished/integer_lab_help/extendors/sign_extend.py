from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements,thirty_two_bit_unsigned_decimal_to_binary_array
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_signed_decimal_to_binary_array import thirty_two_bit_signed_decimal_to_binary_array_no_print_statements

ONE_BYTE = 8
TWO_BYTES = 16
FOUR_BYTES = 32

def sign_extend_intro():
    print("fuck this shit man i just wanna take adderal and goon until i die.")

    """
    typedef enum {
        ONE_BYTE    = 8,
        TWO_BYTES   = 16,
        FOUR_BYTES  = 32,
    } data_size_t;
    
    TEST(test_sign_extend_positive_8_16)
        uint32_t value = 0xABCD'EF30;
        data_size_t from_size = ONE_BYTE;
        data_size_t to_size = TWO_BYTES;
        uint32_t expected_result = 0xABCD'0030;
        uint32_t actual_result = sign_extend(value, from_size, to_size);
        ASSERT_EQUAL(expected_result, actual_result);
    END_TEST
    
    TEST(test_sign_extend_positive_8_32)
        uint32_t value = 0xABCD'EF30;
        data_size_t from_size = ONE_BYTE;
        data_size_t to_size = FOUR_BYTES;
        uint32_t expected_result = 0x0000'0030;
        uint32_t actual_result = sign_extend(value, from_size, to_size);
        ASSERT_EQUAL(expected_result, actual_result);
    END_TEST
    """
    test_1_input_value = 0xABCDEF30
    test_1_expected_result = 0xABCD0030
    test_2_input_value = 0xABCDEF30
    test_2_expected_result = 0x00000030
    print(test_1_input_value)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=test_1_input_value))
    print(test_1_expected_result)
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=test_1_expected_result))


def sign_extend(value, from_size, to_size):
    """
    * Sign-extends a value from a smaller data size to a larger data size.
     *
     * The lower `from_size` bits of `value` are interpreted as a signed integer in
     * two’s-complement representation. Those bits are copied unchanged into the
     * result. Bits between `from_size` and `to_size` are filled with copies of the
     * sign bit (bit `from_size - 1`). All bits above the lower `to_size` bits are
     * unchanged from the original value.
     *
     * For example, sign-extending an 8-bit (`ONE_BYTE`) value to 16 bits
     * (`TWO_BYTES`) copies bit 7 into bits 15..8, while preserving the original
     * lower 8 bits and leaving bits 31..16 unchanged.
     *
     * @pre `to_size` >= `from_size`
     * @pre `to_size` and `from_size` must be 8 (`ONE_BYTE`), 16 (`TWO_BYTES`), or 32 (`FOUR_BYTES`)

    :param value: The original value containing the bits to be extended.
    :param from_size: The size (in bits) of the original signed value.
    :param to_size: The size (in bits) of the destination value.
    :return: The sign-extended value.
    """
    sign_bit = 0
    if from_size == ONE_BYTE:
        #                                         ----------
        #          0b0000'0000'0000'0000'0000'0000'1000'0000
        sign_bit = 0x00000010
    elif from_size == TWO_BYTES:
        #                               ----------
        #          0b0000'0000'0000'0000'1000'0000'0000'0000
        sign_bit = 0x00001000
    else: #four bits
        #            ----------
        #          0b1000'0000'0000'0000'0000'0000'0000'0000
        sign_bit = 0x10000000

    sign_bit = sign_bit & value
    print("\t\t\t\t",thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=sign_bit))

    # Create mask for bits [from_size, to_size) that need to be zeroed

    # Mask with 1s in positions [0, from_size)
    lower_mask = ~(0xFFFFFFFF << from_size) & 0xFFFFFFFF

    # Mask with 1s in positions [to_size, 32)
    if to_size >= 32:  # YOU HAVE TO CHANTGE THIS TO equal(to_size >= 32) IN C BECUASE YOU CAN'T USE LOGICAL OPERATORS. how tf does this benefit me at all?
        upper_mask = 0
    else:
        upper_mask = 0xFFFFFFFF << to_size

    # Combine: keep lower bits and upper bits
    keep_mask = lower_mask | upper_mask

    print("\tlower_mask")
    print("\t\t", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(lower_mask))
    print("\tupper_mask")
    print("\t\t", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(upper_mask))
    print("\tkeep_mask")
    print("\t\t", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(keep_mask))
    print("\tvalue")
    print("\t\t", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(value))
    print()

    return value & keep_mask

if __name__ == '__main__':
    sign_extend_intro()