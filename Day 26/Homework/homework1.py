start = int(input("შეიყვანეთ დასაწყისი რიცხვი: "))
end = int(input("შეიყვანეთ დასასრულის რიცხვი: "))

if end < start:
    print("არასწორი შუალედი")
else:
    total = 0
    print("რიცხვები შუალედში:")
    for number in range(start, end + 1):
        print(number)
        total += number
    print("ჯამი არის:", total)