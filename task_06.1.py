'''
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
'''

import string

search_str = input("Enter search string: ")

letters = string.ascii_letters
start_index = letters.find(search_str[0])
end_index = letters.find(search_str[-1])

if start_index <= end_index:
    print(letters[start_index:end_index+1])


