import string
import keyword

new_variable = input("Enter the new variable: ")
while len(new_variable) == 0:
    new_variable = input("Enter the new variable: ")

res = True
string_punctuation = string.punctuation.replace("_", "")

if new_variable[0].isnumeric():
    res = False

if res:
    count_ = 0
    for letter in new_variable:
        if letter == " " or letter.isupper() or string_punctuation.find(letter) != -1:
            res = False
            break

        if letter == "_":
            count_ += 1
            if count_ > 1:
                res = False
                break
        else:
            count_ = 0

if res:
    if new_variable in keyword.kwlist:
        res = False

print(f"{new_variable} => {str(res)}")

# mock_data = ["_",                       # => True
#              "__",                      # => False
#              "___",                     # => False
#              "x",                       # => True
#              "get_value",               # => True
#              "get value",               # => False
#              "get!value",               # => False
#              "some_super_puper_value",  # => True
#              "Get_value",               # => False
#              "get_Value",               # => False
#              "getValue",                # => False
#              "3m",                      # => False
#              "m3",                      # => True
#              "assert",                  # => False
#              "assert_exception"]        # => True
#
# for i in mock_data:
#     if i[0].isnumeric():
#         print(f"{i} => False")
#         continue
#
#     loop_brek = False
#     count_ = 0
#     for letter in i:
#         if letter == " ":
#             print(f"{i} => False")
#             loop_brek = True
#             break
#         if letter.isupper():
#             print(f"{i} => False")
#             loop_brek = True
#             break
#         if string_punctuation.find(letter) != -1:
#             print(f"{i} => False")
#             loop_brek = True
#         if letter == "_":
#             count_ += 1
#             if count_ > 1:
#                 print(f"{i} => False")
#                 loop_brek = True
#                 break
#         else:
#             count_ = 0
#     if loop_brek:
#         continue
#
#     if i in keyword.kwlist:
#         print(f"{i} => False")
#         continue
#
#     print(f"{i} => True")


