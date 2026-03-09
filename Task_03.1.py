num1=int(input("Введіть число 1: "))
action=input("Введіть дію (+, -, *, /): ")
num2=int(input("Введіть число 2: "))

match action:
    case "+": print(num1+num2)
    case "-": print(num1-num2)
    case "*": print(num1*num2)
    case "/": print(num1/num2 if num2 != 0 else "Ділити на нуль не можна!")