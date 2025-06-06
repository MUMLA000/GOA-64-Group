def greet(text):
    letters = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count

print(greet("Hello World"))