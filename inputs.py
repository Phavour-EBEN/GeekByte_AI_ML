"""

name = input("Enter your name:")
print("Hello, ", name)

age = input("Enter your age:")
age_converted = int(age)
print(type(age_converted))

age_converted_str = str(age_converted)
print(type(age_converted_str))


# Control flows

age  = int(input("Enter your age: "))

if age >=18:
    print("You are an adult")
elif age >=13 and age <=18:
    print("You are a teenager")
else:
    print("You are a minor")

#  Loops
for i in range(10):
    print(i)


# while loops
count = 0
while count < 10:
    print("Counting: ", count)
    count = count + 1
"""

# Functions
"""
def function_name(parameters):
    # block of code
    return value/return_statement


def greet():
    print("Hello, World!")

greet()

def greet_with_name(name):
    print("Hello, ", name)

greet_with_name("Prince")

def add(num1, num2):
    results = num1 + num2
    return results

add(1, 2)
"""


# Error Handling
# try:
    # code that might cause an error
# except:
    # code to run if there an error


# number = int(input("enter a number: "))
# result = 10/number
# print(result)
"""
try:
    number = int(input("enter a number: "))
    result = 10/number
    print(result)
except:
    print("Something is wrong!!")
"""

age = int(input("Enter your age: "))

if age <0:
    raise ValueError("Age cannot be a negative number")
else:
    print("Your age is : ", age)