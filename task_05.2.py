is_continue = True

while is_continue:
    num1=input("Введіть число 1: ")
    while not num1.isnumeric():
        num1 = input("Введіть число 1: ")
    num1=int(num1)

    action_list = ["+", "-", "*", "/"]
    action=input("Введіть дію (+, -, *, /): ")
    while not action in action_list:
        action = input("Введіть дію (+, -, *, /): ")

    num2=input("Введіть число 2: ")
    while not num2.isnumeric():
        num2 = input("Введіть число 2: ")
    num2=int(num2)

    match action:
        case "+": print(num1+num2)
        case "-": print(num1-num2)
        case "*": print(num1*num2)
        case "/": print(num1/num2 if num2 != 0 else "Ділити на нуль не можна!")

    is_continue = True if input("Ви хочете повторити? ") == "y" else False