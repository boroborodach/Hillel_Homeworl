'''
999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
1000 -> 0
423 -> 8
33 -> 9
25 -> 0
1 -> 1
'''

num = input("Enter the number: ")
while not num.isdigit():
    num = input("Enter the number: ")

while True:
    num_str = str(num)
    res = int(num_str[0])
    for i in range(1,len(num_str)):
        res*=int(num_str[i])

    res_str = str(res)

    res_list = list(num_str)
    res_list.append(f"= {res_str}")
    res_str = " * ".join(res_list)
    res_str = res_str.replace("* =", "=")
    print(res_str)

    if res <= 9:
        break
    else:
        num = res