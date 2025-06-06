def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

words_list = ["apple", "banana", "watermelon", "kiwi"]
print(longest_word(words_list))