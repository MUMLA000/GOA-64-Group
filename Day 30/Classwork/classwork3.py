# 3) შექმენით ახალი new_greet ფუნქცია რომელსაც ექნება 2 პარამეტრი: first_name და last_name. 
# ამ ფუნქციამ უნდა დაბეჭდოს შემდეგი ტექსტი: "Greetings [firstname] [lastname]
#  ფუნქცია 2-ჯერ გამოიძახეთ და გადაეცით არგუმენტები.
#  კომენტარებით ახსენით რა განსხვავებაა პარამაეტრებსა და არგუმენტებს შორის

# ფუნქციის აღწერა 2 პარამეტრით: first_name და last_name
def greet(first_name, last_name):
    print(f"hello {first_name} {last_name}")
    print("Welcome")

# ფუნქციის გამოძახება არგუმენტებით
greet("საბა", "მუმლაძე")
greet("გია", "სურამელაშვილი")