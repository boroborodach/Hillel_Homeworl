import string

def is_palindrome(text):
    formated_text = text.lower().strip()
    string_punctuation = string.punctuation + " "
    for char in string_punctuation:
        while formated_text.find(char) != -1:
            formated_text = formated_text.replace(char, "")
    for i in range(len(formated_text)//2):
        if formated_text[i] != formated_text[len(formated_text)-1-i]:
            return False
    return True


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")