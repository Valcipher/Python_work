x = 10
y = 10
z = 20

li1 = [10,20,30]
li2 = [10,20,30]

print(x is y)
print(x is not z)
print(li1 is not li2)

print(id(x))
print(id(y))

print(id(li1))
print(id(li2))

print(10 not in li1)
print(20 in li2)