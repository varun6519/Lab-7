#1(a)
'''n = int(input("Enter N: "))

s = 0

for i in range(1, n + 1):
    s = s + 1 / (2 * i - 1)

print(f"{s:.9f}")'''
#(b)
'''n = int(input("Enter N: "))

s = 0

for i in range(1, n + 1):
    fact = 1

    for j in range(1, 2 * i + 1):
        fact = fact * j

    s = s + 1 / fact

print(f"{s:.9f}")'''
#(c)
'''n = int(input("Enter N: "))

s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        s = s - 1 / (i ** 3)
    else:
        s = s + 1 / (i ** 3)

print(f"{s:.9f}")'''
#(d)
'''n = int(input("Enter N: "))
x = float(input("Enter x: "))

s = 0

for i in range(n):
    power = 2 * i
    fact = 1

    for j in range(1, power + 1):
        fact = fact * j

    s = s + (x ** power) / fact

print(f"{s:.9f}")'''
#(e)
'''n = int(input("Enter N: "))
x = float(input("Enter x: "))

s = 0

for i in range(1, n + 1):
    s = s + (x ** i) / (2 * i - 1)

print(f"{s:.9f}")'''
#2(a)
'''e = float(input("Enter error: "))

s = 0
n = 1

while True:
    old = s

    s = s + (1 / 3) ** n

    if abs(s - old) < e:
        break

    n = n + 1

print("Sum =", s)
print("Number of terms =", n)'''
#(b)
'''x = float(input("Enter x: "))
e = float(input("Enter error: "))

s = 0
fact = 1
power = 1
n = 0

while True:
    old = s

    if n == 0:
        term = 1
    else:
        power = power * x
        fact = fact * n
        term = power / fact

    s = s + term

    if abs(s - old) < e:
        break

    n = n + 1

print("Sum =", s)
print("Number of terms =", n + 1)'''
#(c)
'''x = float(input("Enter x: "))
e = float(input("Enter error: "))

s = 0
n = 1

while True:
    old = s

    term = (x ** n) / n

    if n % 2 == 0:
        s = s - term
    else:
        s = s + term

    if abs(s - old) < e:
        break

    n = n + 1

print("Sum =", s)
print("Number of terms =", n)'''
#3
'''x = int(input())
y = int(input())

total = 0

for i in range(x, y + 1):

    temp = i
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    if i == rev:
        total = total + i

print(total)'''
#4(a)
'''n = int(input("Enter N: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()'''
#(b)
'''n = int(input("Enter N: "))

for i in range(1, n + 1):

    for j in range(n - i):
        print("  ", end="")

    for j in range(i):
        print(chr(65 + j), end=" ")

    print()'''
#(c)
'''n = int(input("Enter N: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")

    print()'''
#(d)
'''n = int(input("Enter N: "))

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()'''
#5
'''n = int(input("Enter N: "))

row = [1]

for i in range(n):

    for j in range(n - i - 1):
        print(" ", end=" ")

    for j in row:
        print(j, end=" ")

    print()

    new = [1]

    for j in range(len(row) - 1):
        new.append(row[j] + row[j + 1])

    new.append(1)

    row = new'''
#6
'''import math

n = int(input("Enter N: "))

s = 0

for i in range(n):

    if i % 2 == 0:
        s = s + 1 / (2 * i + 1)
    else:
        s = s - 1 / (2 * i + 1)

pi = 4 * s

print(f"Approximate pi = {pi:.9f}")

print("Absolute difference =", abs(pi - math.pi))'''
#7
'''n = int(input("Enter N: "))

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()'''
#8
'''s = int(input())
d = int(input())
t = int(input())

total = 0
month = 0
saving = s

while total < t:

    total = total + saving

    month = month + 1

    saving = saving + d

print(month)
print(total)'''
#9
'''n = int(input("Enter N: "))

term = 0
total = 0

for i in range(n):

    term = term * 10 + 1

    total = total + term

print(total)'''
#10
'''n = int(input("Enter N: "))

for i in range(1, n + 1):

    temp = i
    total = 0

    while temp > 0:

        digit = temp % 10

        fact = 1

        for j in range(1, digit + 1):
            fact = fact * j

        total = total + fact

        temp = temp // 10

    if total == i:
        print(i)'''





























