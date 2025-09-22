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
    total_sum = x + y + z
    return total_sum


# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)
