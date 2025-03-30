# 5 ცვლადი, რომლებიც შეიცავს როგორც შედარების, ისე ლოგიკური ოპერატორების კომბინაციას:

exam_score = 85
passing_score = 50
bonus_points = 10
attendance_rate = 90
required_attendance = 80

result1 = exam_score > passing_score and bonus_points > 5  
# True - ქულა აღემატება გასავლელ ზღვარს და ბონუს ქულებიც 5-ზე მეტია.

result2 = exam_score + bonus_points >= 95 or attendance_rate >= required_attendance  
# True - საბოლოო ქულა 95-ს უდრის (85 + 10), რაც საკმარისია, ან დასწრება მოთხოვნილ ზღვარს სცდება.

result3 = exam_score < 40 and attendance_rate < required_attendance  
# False - ქულა 40-ზე მეტი აქვს, ამიტომ სრული პირობა არ შესრულდა.

result4 = not (exam_score < passing_score or attendance_rate < required_attendance)  
# True - არც ქულაა ნაკლები, არც დასწრება, ამიტომ მთლიანობა True გამოდის.

result5 = exam_score == 100 and bonus_points == 0  
# False - ქულა 100 არ არის, ამიტომ ეს პირობა არ სრულდება.

# შედეგების დაბეჭდვა
print(result1)  # True
print(result2)  # True
print(result3)  # False
print(result4)  # True
print(result5)  # False