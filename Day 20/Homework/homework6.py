total = 0
count = 0

number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    total += number
    count += 1
    number = int(input("Enter a number (-1 to stop): "))

if count > 0:
    average = total / count
    print("Average is:", average)
else:
    print("No numbers entered.")