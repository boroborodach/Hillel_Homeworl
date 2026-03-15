import string

new_hashtag = input("Enter new hashtag: ")

new_hashtag = new_hashtag.strip()

string_punctuation = string.punctuation
for char in new_hashtag:
    if char in string_punctuation:
        new_hashtag = new_hashtag.replace(char, "")

list = new_hashtag.split(" ")
empty_count = list.count("")
for _ in range(empty_count):
    list.remove("")

for i in range(len(list)):
    list[i] = list[i].title()
list.insert(0, "#")

res = "".join(list)
new_hashtag = res[:140+1]
print(new_hashtag)