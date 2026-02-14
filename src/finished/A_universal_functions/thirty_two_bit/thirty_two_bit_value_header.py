import math

thirty_two_bit_value_header = \
[math.pow(2,31), math.pow(2,30), math.pow(2,29), math.pow(2,28)," ",
 math.pow(2,27), math.pow(2,26), math.pow(2,25), math.pow(2,24)," ",
 math.pow(2,23), math.pow(2,22), math.pow(2,21), math.pow(2,20)," ",
 math.pow(2,19), math.pow(2,18), math.pow(2,17), math.pow(2,16)," ",
 math.pow(2,15), math.pow(2,14), math.pow(2,13), math.pow(2,12)," ",
 math.pow(2,11), math.pow(2,10), math.pow(2,9), math.pow(2,8)," ",
 math.pow(2,7),  math.pow(2,6),  math.pow(2,5),  math.pow(2,4)," ",
 math.pow(2,3),  math.pow(2,2),  math.pow(2,1),  math.pow(2,0)," ",]

if __name__ == '__main__':
    print(thirty_two_bit_value_header)