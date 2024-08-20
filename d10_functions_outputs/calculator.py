def calculator(x,y,operation):
    if operation == '+':
        return int(x)+int(y)
    elif operator == '-':
        return int(x)-int(y)
    elif operator == '*':
        return int(x)*int(y)
    elif operator == '/':
        return int(x)/int(y)
    else:
        return "pick right operator"

still_calculate = True
num1 = input("What's the first number? ")

while still_calculate == True:    
    operator = input("+ \n - \n * \n / \n Pick an operator: ")
    num2 = input("What's the second number? ")
    result = calculator(num1,num2,operator)
    calc = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
    if calc == 'y':
        still_calculate = True
        num1 = result
    else:
        still_calculate = False
        print(f"Final result is {result}")
