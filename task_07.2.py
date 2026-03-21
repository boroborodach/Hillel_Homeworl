def correct_sentence(text):
    text_list = text.split(".")
    for i in range(len(text_list)):
        if text_list[i] == '':
            continue
        text_list[i] = text_list[i].lower().strip()
        text_list[i] = text_list[i][0].upper() + text_list[i][1:]
    empty_count = text_list.count("")
    for i in range(empty_count):
        text_list.remove("")
    res = ". ".join(text_list)
    return res if res[-1] == "." else res + "."

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')