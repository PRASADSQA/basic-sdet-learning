#Exercise 1
weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    convert = weight / 0.45
    print("weight in lbs: " + str(convert))
else:
    convert = weight * 0.45
    print("weight in kg: " + str(convert))