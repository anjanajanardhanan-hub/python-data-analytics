# 1) Area of a Triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))

if base > 0 and height > 0:
    area = 0.5 * base * height
    print("Area of triangle:", area)
else:
    print("Invalid input")


# 2) Perimeter of a Circle
radius = int(input("Enter radius: "))

if radius > 0:
    perimeter = 2 * 3.14 * radius
    print("Perimeter of circle:", perimeter)
else:
    print("Invalid radius")


# 3) Square of a Number
a = int(input("Enter number: "))

if a >= 0:
    print("Square:", a * a)
else:
    print("Number is negative")


# 4) Convert Dollar to INR
dollar = float(input("Enter dollar: "))

if dollar > 0:
    print("INR:", dollar * 88)
else:
    print("Invalid amount")


# 5)Miles to Kilometres Conversion
miles = float(input("Enter miles: "))

if miles >= 0:
    print("KM:", miles * 1.609)
else:
    print("Invalid distance")


# 6) Check Positive or Negative
a = int(input("Enter number: "))

if a > 0:
    print("Positive")
else:
    print("Negative")


# 7) Check Whether a Number Is a Multiple of 5
a = int(input("Enter number: "))

if a % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


# 8) find the largest among three numbers.
a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
c = int(input("Enter a number3: "))

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")
