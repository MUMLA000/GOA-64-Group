even_count = 0
odd_count = 0

num_positive = True

while num_positive:
    number = int(input("Enter a number: "))
    if number < 0:
        num_positive = False
    elif number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)