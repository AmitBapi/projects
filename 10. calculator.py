def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : devide}

def calculator():
    should_continue = True
    f_num = float(input("what is the first number : "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symb = input("pick an operation : ")
        s_num= float(input("what is the second number : "))
        answer = (operations[operation_symb](f_num, s_num))
        print(f"the result is :{answer}")
        
        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ")
        
        if choice == "y":
            f_num = answer
        else:
            should_continue = False
            # print("\n"*30)
            # calculator()

calculator()
