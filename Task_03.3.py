list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1]
list_5 = []

active_list = list_5.copy()

res = []
if len(active_list) <= 1:
    res.append(active_list)
    res.append([])
else:
    middle = len(active_list) // 2
    middle = middle + 1 if len(active_list) % 2 != 0 else middle
    res.append(active_list[:middle])
    res.append(active_list[middle:])

print(res)