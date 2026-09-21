# CONDITIONAL STATEMENTS
# A conditional statement is used to make a decision in a Python program.
# The basic form is

# if condition:
#     statement
# else:
#     statement

# example
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# check even or odd numbers
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# elif STATEMENT
# We use elif when we have more than two conditions to check.
# if condition1:
#     statement
# elif condition2:
#     statement
# else:
#     statement

# example
smark = 85
if smark > 95:
    print("E")
elif smark > 90:
    print("A")
elif smark > 60:
    print("B")
elif smark > 20:
    print("C")
else:
    print("fail")

    # eg 2
a = int(input("Enter a num: "))
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")
