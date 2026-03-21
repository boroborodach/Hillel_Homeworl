def common_elements():
    multiples_list_3 = []
    multiples_list_5 = []
    for i in range(100+1):
        if i % 3 == 0:
            multiples_list_3.append(i)

        if i % 5 == 0:
            multiples_list_5.append(i)

    multiples_set_3 = set(multiples_list_3)
    multiples_set_5 = set(multiples_list_5)
    res = multiples_set_3.intersection(multiples_set_5)
    return res


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")