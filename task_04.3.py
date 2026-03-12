import random

random_len = random.randint(3, 10)

list_1 = []
for _ in range(random_len+1):
    list_1.append(random.randint(1, 10))

list_2 = []
list_2.append(list_1[0])
list_2.append(list_1[2])
list_2.append(list_1[-2])

print(list_1, list_2, sep=" == ")