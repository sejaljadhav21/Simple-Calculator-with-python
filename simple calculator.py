while True:
    print("Enter 'x' to exit")
    a = input("Enter first number: ")
    if a == 'x':
        break
    operator = input("Enter an operator +,-,/,//,*,** : ")
    b = input("Enter second number: ")
    if operator == '+':
        result = float(a) + float(b)
    elif operator == '-':
        result = float(a) - float(b)
    elif operator == '/':
        result = float(a) / float(b)
    elif operator == '//':
        result = float(a) // float(b)
    elif operator == '*':
        result = float(a) * float(b)
    elif operator == '**':
        result = float(a) ** float(b)
    else:
        print("Invalid Operator")
        continue
    print(a, operator, b, '=', result)
