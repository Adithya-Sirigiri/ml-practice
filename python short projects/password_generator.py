'''
import random
import string
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)
print("Welcome to password generator!!\n")
l=int(input("How many letters would you like in your password:\n"))
for i in range(0,l):
    for x in random.choice(letters):#it gives you a single letter
        a=list(x)
s=int(input("How many symbols would you like in your password:\n"))
for j in range(0,s):
    for y in random.choice(symbols):
        b=list(y)
n=int(input("How many numbers would you like in your password:\n"))
for k in range(0,n):
    for z in random.choice(numbers):
        c=list(z)


f=[a,b,c]
random.shuffle(f)#it doesnot return anything

for k in f:
    print(k)
'''
import random
import string
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)
print("Welcome to password generator!!\n")
l = int(input("How many letters would you like in your password:\n"))
s = int(input("How many symbols would you like in your password:\n"))
n = int(input("How many numbers would you like in your password:\n"))
a = []
for i in range(l):
    x = random.choice(letters)
    a.append(x)
b = []
for j in range(s):
    y = random.choice(symbols)
    b.append(y)
c = []
for k in range(n):
    z = random.choice(numbers)
    c.append(z)
f = a + b + c
random.shuffle(f)
password = ''.join(f)
print("\nHere is your password:", password)