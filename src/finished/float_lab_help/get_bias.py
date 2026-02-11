import math

def get_bias_from_IEEE_exponent_bit_emount(bits):
    """
    bias = 2 ^ (k - 1) − 1
        k = bits in the exponent field
            not the fucking bit rate. like 8 16 32 or 64

    single precision = 8 bits in exponent
    double precision = 11 bits in exponent
    half precision = 5 bits in exponent
    quad precision = 15 bits in exponent
    """
    return math.pow(2, bits - 1) - 1

if __name__ == "__main__":
    print(get_bias_from_IEEE_exponent_bit_emount(8))