#!/usr/bin/python3

x = 1000000000
for i in range(1000000):
    x += 0.000001
x -= 1000000000
print(x) # 0.95367431640625

def t(x):
    y = x
    for i in range(1000000):
        x += 0.000001
    return x - y

for i in range(1, 40):
    x = 2 ** i
    print(i, t(x))
