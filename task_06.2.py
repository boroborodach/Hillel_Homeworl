'''
0 -> 0 днів, 00:00:00
224930 -> 2 дні, 14:28:50
466289 -> 5 днів, 09:31:29
950400 -> 11 днів, 00:00:00
1209600 -> 14 днів, 00:00:00
1900800 - > 22 дні, 00:00:00
8639999 -> 99 днів, 23:59:59
22493 -> 0 днів, 06:14:53
7948799 -> 91 день, 23:59:59
'''

sec = input("Enter the time in seconds: ")
while not sec.isdigit():
    sec = input("Enter the time in seconds: ")

sec = int(sec)
if 0 <= sec < 8640000:
    days = sec // 86400
    sec-= days * 86400
    hours = sec // 3600
    sec-= hours * 3600
    minutes = sec // 60
    sec-= minutes * 60

    print(f"{days} days, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")