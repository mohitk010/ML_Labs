def add(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def substract(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def multiply(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def add_3_nums(x,y,z):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    total_sum = x + y + z
    return x + y + z


# f1_op = add(2,3)
# f2_op = substract(2,3)
# f3_op = multiply(2,3)
# f4_op = add_3_nums(f1_op,f2_op,f3_op)

# print( f1_op)
# print(f2_op)
# print(f3_op)
# print(f4_op)
