list_1 = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
list_2 = [0] #-> [0]
list_3 = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

active_list = list_4.copy()
search_value = 0

if len(active_list) <= 1:
    print(active_list)
else:
    count = active_list.count(search_value)
    for _ in range(count):
        active_list.remove(search_value)
        active_list.append(search_value)
    print(active_list)