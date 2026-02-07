from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_unsigned_decimal_to_binary_array import thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements,thirty_two_bit_unsigned_decimal_to_binary_array
from src.decimal_to_binary.thirty_two_bit.thirty_two_bit_signed_decimal_to_binary_array import thirty_two_bit_signed_decimal_to_binary_array_no_print_statements

ONE_BYTE = 8
TWO_BYTES = 16
FOUR_BYTES = 32

def sign_extend_intro():
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
    print(thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=sign_extend(value=test_1_input_value,from_size=ONE_BYTE,to_size=TWO_BYTES)))


def sign_extend(value, from_size, to_size):
    """
    Sign-extends a value from a smaller data size to a larger data size.

    The lower `from_size` bits of `value` are interpreted as a signed integer in
    two's-complement representation. Those bits are copied unchanged into the
    result. Bits between `from_size` and `to_size` are filled with copies of the
    sign bit (bit `from_size - 1`). All bits above the lower `to_size` bits are
    unchanged from the original value.
    """

    print("\n=== SIGN EXTEND DEBUG ===")
    print(f"from_size={from_size}, to_size={to_size}")
    print(f"\nOriginal value: 0x{value:08X}")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=value))

    # Determine shift amount to move sign bit to MSB position
    if from_size == 8:
        shift_left = 24
    elif from_size == 16:
        shift_left = 16
    else:  # from_size == 32
        shift_left = 0

    print(f"\nshift_left = {shift_left} (to move bit {from_size - 1} to bit 31)")

    # Shift sign bit to MSB position (bit 31)
    temp = value << shift_left
    print(f"\nAfter shifting left by {shift_left}:")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=temp & 0xFFFFFFFF))

    # Mask to 32 bits
    temp = temp & 0xFFFFFFFF

    # Check the sign bit
    sign_bit = (temp >> 31) & 1
    print(f"Sign bit (bit 31): {sign_bit}")

    # Convert to signed integer for arithmetic right shift
    # In Python, we need to manually handle the sign bit
    if temp & 0x80000000:  # If MSB is 1 (negative)
        print("Sign bit is 1 - doing arithmetic right shift (fill with 1s)")
        # Arithmetic right shift: fill with 1s
        temp = temp | (0xFFFFFFFF << 32)  # Extend sign for Python's arbitrary precision
        signed_temp = temp - (1 << 32)  # Convert to negative
        print(f"Treated as signed: {signed_temp}")
    else:
        print("Sign bit is 0 - doing logical right shift (fill with 0s)")
        signed_temp = temp
        print(f"Treated as signed: {signed_temp}")

    # Shift back right (arithmetic shift in Python for negative numbers)
    signed_temp = signed_temp >> shift_left
    print(f"\nAfter arithmetic shifting right by {shift_left}: {signed_temp}")

    # Convert back to unsigned 32-bit
    temp = signed_temp & 0xFFFFFFFF
    print(f"As unsigned 32-bit: 0x{temp:08X}")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=temp))

    # Create mask for the region [from_size, to_size) that needs sign extension
    lower_mask = ~(0xFFFFFFFF << from_size) & 0xFFFFFFFF  # Keep bits [0, from_size)
    print(f"\nlower_mask (keep bits [0, {from_size})):")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=lower_mask))

    if to_size >= 32:
        upper_mask = 0
    else:
        upper_mask = 0xFFFFFFFF << to_size  # Keep bits [to_size, 32)

    upper_mask = upper_mask & 0xFFFFFFFF
    print(f"\nupper_mask (keep bits [{to_size}, 32)):")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=upper_mask))

    extension_mask = ~(lower_mask | upper_mask) & 0xFFFFFFFF  # Bits [from_size, to_size) to fill
    print(f"\nextension_mask (fill bits [{from_size}, {to_size}) with sign):")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=extension_mask))

    # Combine: keep original lower bits, sign-extended middle bits, original upper bits
    print(f"\nCombining parts:")
    print(f"  value & lower_mask = keep original bits [0, {from_size}):")
    print("  Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=value & lower_mask))

    print(f"  temp & extension_mask = sign-extended bits [{from_size}, {to_size}):")
    print("  Binary: ",
          thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=temp & extension_mask))

    print(f"  value & upper_mask = keep original bits [{to_size}, 32):")
    print("  Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=value & upper_mask))

    result = (value & lower_mask) | (temp & extension_mask) | (value & upper_mask)
    result = result & 0xFFFFFFFF

    print(f"\nFinal result: 0x{result:08X}")
    print("Binary: ", thirty_two_bit_unsigned_decimal_to_binary_array_no_print_statements(decimal=result))
    print("=== END DEBUG ===\n")

    return result

if __name__ == '__main__':
    sign_extend_intro()