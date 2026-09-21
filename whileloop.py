# while LOOP
# A while loop is used to repeat a block of code while a condition is true.
# Basic structure
# while condition:
# statement

# eg 1) print numbers from 1 to 9
i = 1
while i < 10:
    print(i)
    i = i + 1


# 2) find the sum of numbers from 1 to n using a while loop.
n = int(input("Enter a number: "))
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print(s)


# 3) Sum of even numbers and odd numbers from 1 to 100.
i = 1
even = 0
odd = 0
while i <= 100:
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
    i = i + 1
print(even, odd)


# 4) factorial of a number using a while loop.
n = int(input("Enter a number: "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)

# 5) find sum of all digits of number 15324
num = 15324
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)
