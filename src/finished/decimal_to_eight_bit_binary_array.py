import math

def decimal_to_eight_bit_binary_array(decimal, tab_amount="\t"):
    print(tab_amount,"decimal_to_binary")
    tab_amount += "\t"

    return_array = []

    four_bit_readability_counter = 0

    # the reason it has to be a certain bit values is because of my methods
    # when you want to go from 4bits to 8 bits or whatever. go here.
    n = 7
    print(tab_amount, "n = ", n)

    # yeah yeah i know.
    infinite_loop_counter = 0
    print(tab_amount, "infinite_loop_counter = ", infinite_loop_counter)

    while decimal >= 0 and n >= 0 and infinite_loop_counter < 20:
        print(tab_amount + "\t", "while iteration")
        print(tab_amount + "\t\t", "Ox_decimal = ", decimal)

        if four_bit_readability_counter == 4:
            return_array.append(" ")
            four_bit_readability_counter = 0

        print(tab_amount + "\t\t", "Ox_decimal - 2^n > 0")
        print(tab_amount + "\t\t", decimal, "-", (math.pow(2, n)), "> 0")
        print(tab_amount + "\t\t", (decimal - (math.pow(2, n))), "> 0")
        print(tab_amount + "\t\t", (decimal - (math.pow(2, n))) > 0)
        print()
        print(tab_amount + "\t\t return_array = ", return_array)
        print(tab_amount + "\t\t ->")
        if (decimal - (math.pow(2, n))) >= 0:
            decimal = decimal - math.pow(2, n)
            return_array.append(1)
        else:
            return_array.append(0)
        print(tab_amount + "\t\t return_array = ", return_array)
        print()

        n -= 1
        print(tab_amount + "\t\t", "n = ", n)

        four_bit_readability_counter += 1
        print(tab_amount + "\t\t", "four_bit_readability_counter = ", four_bit_readability_counter)

        infinite_loop_counter += 1
        print(tab_amount + "\t\t", "infinite_loop_counter = ", infinite_loop_counter)
        print()
        print(tab_amount + "\t\t", "decimal > 0", " ", "n >= 0" , " ", "infinite_loop_counter < 20")
        print(tab_amount + "\t\t", decimal, "> 0", " ", n, ">= 0" , " ", infinite_loop_counter, "< 20")
        print(tab_amount + "\t\t", decimal > 0, " ", n >= 0 , " ", infinite_loop_counter < 20)
        print()

    return return_array

def decimal_to_eight_bit_binary_array_no_print_statements(decimal):

    return_array = []

    four_bit_readability_counter = 0

    # the reason it has to be a certain bit values is because of my methods
    # when you want to go from 4bits to 8 bits or whatever. go here.
    n = 7

    # yeah yeah i know.
    infinite_loop_counter = 0

    while decimal >= 0 and n >= 0 and infinite_loop_counter < 20:

        if four_bit_readability_counter == 4:
            return_array.append(" ")
            four_bit_readability_counter = 0

        if (decimal - (math.pow(2, n))) >= 0:
            decimal = decimal - math.pow(2, n)
            return_array.append(1)
        else:
            return_array.append(0)

        n -= 1

    return return_array

if __name__ == "__main__":
    print(decimal_to_eight_bit_binary_array(12))