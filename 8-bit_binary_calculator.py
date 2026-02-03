"""
8-bit binary calculator

in C you can just do this but uhm....
fuck c. lets be honest with ourselves
this will have GUI so i can see wtf is happening

hex table
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMkM_F_xDscBtvlHpBzQRS9s030WxdQa8lEg&s

"""
import math


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

    four_bit_readability_counter = 0
    print(tab_amount,"four_bit_readability_counter = ",four_bit_readability_counter)

    #the reason it has to be a certain bit values is because of my methods
    #when you want to go from 4bits to 8 bits or whatever. go here.
    n = 7
    print(tab_amount,"n = ",n)

    #yeah yeah i know.
    infinite_loop_counter = 0
    print(tab_amount,"infinite_loop_counter = ",infinite_loop_counter)

    while Ox_decimal > 0 and n >= 0 and infinite_loop_counter < 20:
        print(tab_amount+"\t","Ox_decimal = ",Ox_decimal)

        if four_bit_readability_counter == 4:
            return_array.append(" ")
            four_bit_readability_counter = 0

        print(tab_amount+"\t","Ox_decimal - 2^n > 0")
        print(tab_amount+"\t",Ox_decimal ,"-", (math.pow(2,n)),"> 0")
        print(tab_amount+"\t",( Ox_decimal - (math.pow(2, n)) ),"> 0")
        print(tab_amount+"\t",( Ox_decimal - (math.pow(2, n)) ) > 0)
        if ( Ox_decimal - (math.pow(2, n)) ) >= 0:
            Ox_decimal = Ox_decimal - math.pow(2, n)
            return_array.append(1)
        else:
            return_array.append(0)

        n -= 1
        print(tab_amount+"\t","n = ",n)

        four_bit_readability_counter += 1
        print(tab_amount+"\t","four_bit_readability_counter = ",four_bit_readability_counter)

        infinite_loop_counter += 1
        print(tab_amount+"\t","infinite_loop_counter = ",infinite_loop_counter)
        print()

    return return_array



def get_eight_bit_unsigned_flippy_do_row_array(tab_amount="\t"):
    return [128,64,32,16,8,4,2,1]

def eight_bit_Ox_add(Ox1, Ox2, tab_amount="\t"):
    print(tab_amount,"eight_bit_0x_add")
    tab_amount += "\t"
    Ox1_array = Ox_eight_bit_to_binary_array(Ox=Ox1,tab_amount=tab_amount+"\t")
    Ox2_array = Ox_eight_bit_to_binary_array(Ox=Ox2,tab_amount=tab_amount+"\t")



if __name__ == "__main__":
    Ox_variable = 0xFF
    print(Ox_eight_bit_to_binary_array(Ox=Ox_variable, tab_amount="\t"))
