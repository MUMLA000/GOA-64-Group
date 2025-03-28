# წიგნების თავდაპირველი ფასები
book1_price = 30  # პირველი წიგნის ფასი
book2_price = 40  # მეორე წიგნის ფასი
book3_price = 50  # მესამე წიგნის ფასი
book4_price = 60  # მეოთხე წიგნის ფასი
book5_price = 70  # მეხუთე წიგნის ფასი

# ფასდაკლების ოდენობა (პროცენტებში)
discount = 20  # ფასდაკლება 20%

# ფასდაკლებული წიგნების ახალი ფასები
book1_new_price = book1_price - (book1_price * discount / 100)
book2_new_price = book2_price - (book2_price * discount / 100)
book3_new_price = book3_price - (book3_price * discount / 100)
book4_new_price = book4_price - (book4_price * discount / 100)
book5_new_price = book5_price - (book5_price * discount / 100)

# ახალი ფასების დაბეჭდვა
print("პირველი წიგნის ახალი ფასი:", book1_new_price)
print("მეორე წიგნის ახალი ფასი:", book2_new_price)
print("მესამე წიგნის ახალი ფასი:", book3_new_price)
print("მეოთხე წიგნის ახალი ფასი:", book4_new_price)
print("მეხუთე წიგნის ახალი ფასი:", book5_new_price)
