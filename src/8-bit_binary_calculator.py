"""
8-bit binary calculator

in C you can just do this but uhm....
fuck c. lets be honest with ourselves
this will have GUI so i can see wtf is happening

hex table
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMkM_F_xDscBtvlHpBzQRS9s030WxdQa8lEg&s

TODO: finish the fucking thing.

"""





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
