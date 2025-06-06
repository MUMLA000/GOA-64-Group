def sum_even_numbers(array):
    even_sum = 0
    for number in array:
        remainder = number % 2
        if remainder == 0:
            even_sum += number
    
    print(even_sum)

sum_even_numbers([10, 11, 12, 13, 14, 15, 16, 17, 18 , 19, 20])



def simple():
    print("Result")

    return 123

simple_result = simple()

print(f"Value of simple_result variable: {simple_result}")



def greeting():
    return "Hellow, welcome to my program"

print (greeting())



def add_numbers(num1=0, num2=0):
    return num1 + num2
print(add_numbers(10))
print(add_numbers(20, 45))
print(add_numbers())






def rectangle(width, length):
    area = width * length
    perimeter = 2 * (width + length)
    return area, perimeter

result = rectangle (5, 8)

print(result)


