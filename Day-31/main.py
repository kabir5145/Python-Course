# The values in sets are unordered, unchangeable, and do not allow duplicate values.

info = {"kabir",19,True, 4.2, 19}
print(info)

k = set()
print(type(k))
k.add("kabir")
k.add(19)
k.add(True)
k.add(4.2)
print(k)

for i in info:
    print(i)