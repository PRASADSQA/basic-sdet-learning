name = "Hello world"
age = 35
price = 19.9
is_sdet = True

print(name)
print(age)
print(price)
print(is_sdet)

# Receiving Inputs
name = input("What is your name? ")
print("Hello " + name)

# Type Conversion
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year) 
print(age)

first_number = float(input("Enter first number? "))
second_number = float(input("Enter second number? "))
sum = first_number + second_number
print("Sum: " + str(sum))

# #strings
course = 'Python for Begineers'
print(course.upper())
print(course.find('y'))
print(course.find('for'))
print(course.replace('for','4'))
print('Python' in course)

# #Arithmetic Operators
print(10 + 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
X = 10
Y = X + 2
print(Y)
X += 3
print (X)
X *= 3
print (X)
x = 10 + 3 * 2
y = (10 + 3) * 2
print(x)
print(y)

# #comparison operators (>, >=, <, <=, ==, !=)
a = 3 > 2
print(a)
a = 3 != 2
print(a)
a = 3 == 2
print(a)

# #Logical Operators
price = 25
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print(not price < 30)

#if Statement
temp = int(input("give today temperature? ")) 
if temp > 30:
    print("it's a hot date")
    print("Drink water")
elif temp > 20:
    print("it's a good date")
elif temp >= 10:
    print ("it's bit cold")
else:
    print("it freezing") 

#Exercise
weight = float(input("Weight: "))
unit = input ("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs:" + str(converted))

#While Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

i = 10
while i >= 0:
    print(i * '*')
    i = i - 1

#Lists
