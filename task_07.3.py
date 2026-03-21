def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    last_text = text[first_index+1:]
    second_index = last_text.find(some_str)
    if second_index == -1:
        return None
    return first_index + second_index + 1



assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')