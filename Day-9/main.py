# Typecasting in python

a = "1"
b = "2"
c = a + b  
print(int(a) + int(b))  # Output: "3"
print(int(c))  # Output: "12"

x = 1
y = 2.5
print(float(x) + y)  # Output: 3.5
print(str(x) + str(y))  # Output: "12.5"

# Implicit typecasting
m = 5
n = 2.9
result = m + n  # m is implicitly converted to float
print(result)  # Output: 7.0