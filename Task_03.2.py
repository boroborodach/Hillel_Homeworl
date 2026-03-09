list_1 = [12, 3, 4, 10]
list_2 = [1]
list_3 = []
list_4 = [12, 3, 4, 10, 8]
list_5 = [12, 3]

action_list = list_5

if len(action_list) == 0 or len(action_list) == 1:
    print("З пустим або списком з одного елементу неможливо виконати переміщення елементів")
elif len(action_list) == 2:
    action_list.reverse()
    print(action_list)
else:
    last_el =action_list[-1]
    first_el = action_list[0]
    action_list.remove(first_el)
    action_list.pop(-1)
    action_list.append(first_el)
    action_list.insert(0,last_el)
    print(action_list)
