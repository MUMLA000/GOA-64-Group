# 2) შექმენით ერთი ცვლადი რომელშიც შეინახავთ თქვენს 
# სრულ სახელსა და გვარს, ამ სიტყბების პირველი ასოები უნდა იყოს დიდი.
#  შემდეგ for ციკლის მეშვეობით გადაურეთ თქვენს სრულ სახელს და შეამოწმეთ 
# სახელის და გვარის პირველი ასოები თუ დიდი, მათთან აიღეთ კიდევ 3 სხვა დიდი 
# სიმბოლო თქვენი სრული სახელიდან და შეამოწმეთ ასეთი თუ გხვდებათ თქვენი 
# სახელიდან, თუ ასეა მაშინ result ცვლადს (რომელსაც შექმნით for ციკლის 
# გამოყენებამდე და შეინახავთ ცარიელ სტრინგს) დაამატეთ 
# ამ ასოების პატარა ვერსია მაგ: (თუ char == "A": result += "a" 



full_name = "Ana Bella Cooper Dylan Eric"

result = ""

uppercase_letters = [ch for ch in full_name if ch.isupper()]

selected_letters = uppercase_letters[:5]

for ch in full_name:
    if ch in selected_letters:
        result += ch.lower()

print("Selected letters in lowercase:", result)