even_count = 0
odd_count = 0

number = int(input("Enter a number: "))

while number >= 0:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = int(input("Enter a number: "))

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)