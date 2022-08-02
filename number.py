a = int(input("a: "))
b = int(input("b: "))
operator = input("+ - * / : ")

if(operator == "+"):
    result = a + b
    print(f"{a} + {b} = {result}")
elif(operator == "-"):
    result = a - b
    print(f"{a} - {b} = {result}")
elif(operator == "*"):
    result = a * b
    print(f"{a} * {b} = {result}")
elif(operator == "/"):
    result = a / b
    print(f"{a} / {b} = {result}") 
else:
    print("The operator doesn't available")