# vowels = "aeiou"
sentence = input("Enter a Sentence: ")
consonant_count = 0
vowel_count = 0
length = 0
for char in sentence:
    if char == "a" or char == "A":
        vowel_count += 1
    elif char == "e" or char == "E":
        vowel_count += 1
    elif char == "i" or char == "I":
        vowel_count += 1
    elif char == "o" or char == "O":
        vowel_count += 1
    elif char == "u" or char == "U":
        vowel_count += 1
    else:
        consonant_count += 1
    length += 1

print(f"Vowels in total: {vowel_count}")
print(f"Consonant in total: {consonant_count}")
