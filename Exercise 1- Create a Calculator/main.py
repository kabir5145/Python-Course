# Creating a calculator 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a + b
subtract = a - b
multiply = a * b
divide = a / b if b != 0 else "Undefined (division by zero)"
remainder = a % b if b != 0 else "Undefined (modulus by zero)"

print("Addition: ", add)
print("Subtraction: ", subtract)
print("Multiplication: ", multiply)
print("Division: ", divide)
print("Remainder: ", remainder)