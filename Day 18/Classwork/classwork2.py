# 2) მოხმარებელს შემოატანინეთ თავისი გამოცდის ქულა,
#  შემდეგ პირობითი განხცადების საშვალებით შეამოწმეთ ეს ქულა მეტია თუ 50-ზე,
#  თუ მეტია დაუბეჭდეთ რომ გამოცდა ჩააბარა
score = int(input("შეიყვანე შენი ქულა: "))

if score > 50:
    print("შენ ჩააბარე გამოცდა!")



# BONUS დავალება


score = int(input("შეიყვანე შენი ქულა: "))

if score > 50:
    print("შენ ჩააბარე გამოცდა!")
    print("კაი ბიჭი ხარ!" if score % 2 == 0 else "ტორტი ხარ!")