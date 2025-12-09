# variables of integer type

number1 = 24
number2 = 34
number3, number4, number5 = 50, 70, 100
"""
print(number1)
print(number2)
print(type(number1))

# variables of string type
name = "Nana"
print(name)
print(type(name))

# variables of float type
price_1 = 24.90
price_2 = 24.0
print(price_1)
print(price_2)
print(type(price_2))


# performing some arithmetic operations
print(number1 + number2)

sum = number1 + number2
print(sum)

print(number1 - number2)
print(number2 * number1)
final_result = (number2 / number1)
print(final_result)
print(type(final_result))


# logical operators/comparisons
print(number2 == number4)  #equals to
print(type(number2 == number4))
print(number2 != number4) #not equals to
print(type(number2 != number4)) 

print(number2 > number4) #greater than
print(type(number2 > number4))
print(number2 < number4) #less than
print(type(number2 < number4))
print(number2 >= number4) #greater than or equal to
print(type(number2 >= number4))
print(number2 <= number4) #less than or equal to
print(type(number2 <= number4))
"""

# lists, Dictionaries, Tuples, Sets
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"] #indexs in [0, 1, 2, 3, 4]
# print(cars)

# cars.pop(2)
# print(cars)

cars.remove("Chevrolet")
print(cars)

# Dictionaries
person = {"name": "James", "age": 24, "city": "New York", "country": "USA", "email": "james@example.com"}
print(person)