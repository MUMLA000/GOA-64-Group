correct_pin = "1234"

attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        attempts = 0
    else:
        attempts -= 1
        if attempts == 0:
            print("Access Denied")