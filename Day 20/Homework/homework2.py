positive_sum = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    elif number > 0:
        positive_sum += number
print("The sum of all positive numbers is:", positive_sum)