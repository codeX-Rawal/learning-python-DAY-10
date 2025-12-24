# Day 10: Practice Programs (Revision)

# 1. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 2. Find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

# 3. Sum of numbers from 1 to n
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum from 1 to", n, "is:", sum)

# 4. Multiplication table
num = int(input("Enter number for table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 5. Count digits in a number
number = input("Enter a number: ")
print("Total digits:", len(number))
