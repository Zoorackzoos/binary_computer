def not_equal_into():
    print("not equal bro")
    print("5 != 6", 5 != 6, not_equal_help(5,6))
    print("11 == 11", 11 != 11, not_equal_help(11,11))

def not_equal_help(value1, value2):
    return (value1 ^ value2) != 0

if __name__ == "__main__":
    not_equal_into()
