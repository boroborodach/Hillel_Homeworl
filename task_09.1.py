from string import punctuation as pnct

def popular_words (text, words):
    """
    Counts the occurrences of specific words in a given text.

    :param text: The input string where the search will be performed.
    :type text: str
    :param words: A list of words to be counted in the text.
    :type words: list[str]
    :return: A dictionary where keys are the words and values are their counts.
    :rtype: dict[str, int]
    """
    text = text.lower().strip()
    for ch in pnct:
        while text.find(ch) != -1:
            text = text.replace(ch, "")
    text_list = text.split(" ")

    def count(word):
        nonlocal text_list
        count = 0
        for el in text_list:
            count = count + 1 if el == word else count
        return count

    count_res = list(map(count, words))
    return dict(zip(words, count_res))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
