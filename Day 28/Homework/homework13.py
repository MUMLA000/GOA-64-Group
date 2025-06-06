text = "I visited Georgia"
word = input("შეიყვანე საძიებელი სიტყვა: ")

position = text.find(word)
if position != -1:
    print(position)
else:
    print("word not found")