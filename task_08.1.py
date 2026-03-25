def add_one(some_list):
    num_old = 0
    for i in range(len(some_list)):
        num_old += some_list[i]
        if i != len(some_list) - 1:
            num_old *= 10
    int_num_new = num_old + 1
    res = list(str(int_num_new))

    for i in range(len(res)):
        res[i] = int(res[i])

    return res

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")