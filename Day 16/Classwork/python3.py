# 3) შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს

password = "1234"  

while True:  
    passw = input("შეიყვანე პაროლი: ")  
    if passw == password:  
        print("პაროლი სწორია!")