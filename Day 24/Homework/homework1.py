word = input("შეიყვანეთ სიტყვა: ")

if word == word[::-1]:
    print("ეს განსაკუთრებული სიტყვაა (Palindrome).")
else:
    print("ეს ჩვეულებრივი სიტყვაა.")