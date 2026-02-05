from src.finished.decimal_to_eight_bit_binary_array import decimal_to_eight_bit_binary_array

def Ox_eight_bit_to_binary_array(Ox, tab_amount="\t"):
    print(tab_amount,"Ox_to_binary_array")
    tab_amount += "\t"
    """
    1. Ox -> decimal
        so i can take away 2^n over time
        if the next 2^n can be taken away, take it away and add it to an array as 1
        else: add a 0
    2. for every 4th element. add a " " to the array so it's more readable.

    values from:
        0 -> 255

    :param Ox: this is a hexadecimal value
    :param tab_amount: this is a string that's usually "\t"
    :return: an array of bits that represent a binary value. more visually pleasing  to me
    """
    return_array = []

    print(tab_amount,"Ox = ",Ox)
    #Ox -> decimal
    #OxF1 -> Ob1111'0001
    Ox_decimal = int(Ox)
    print(tab_amount,"Ox_decimal = ",Ox_decimal)

    return_array = decimal_to_eight_bit_binary_array(Ox_decimal, tab_amount=tab_amount)

    return return_array