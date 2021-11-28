## booleans and condition for unit week 3 university of the people

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 * num2

def mul(num1, num2):
    return num1 / num2

def main():
    num1 = int(input("what is number 1?"))
    num2 = int(input("what is number 2?"))
    operation = input("what do you want to do? (add, substract, multiply, and divide)")
    
    if(operation == 'add'):
        print(add(num1, num2))

    elif(operation == 'substract'):
        print(sub(num1, num2))

    elif(operation == 'multiply'):
        print(mul(num1, num2))

    elif(operation == 'divide'):
        print(div(num1, num2))

    else:
        print("i dont understand")

main()