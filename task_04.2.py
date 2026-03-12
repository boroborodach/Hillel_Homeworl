list_1 = [1, 3, 5] #=> 30
list_2 = [6] #=> 36
list_3 = [] #=> 0

active_list = list_3.copy()

summ = 0
if len(active_list) > 0:
    for i in range(0, len(active_list), 2):
        summ += active_list[i]
    summ *= active_list[-1]
print(summ)