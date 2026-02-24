# try:
#     a = int(input("Enter the number : "))

#     print(f"Multiplication table of {a} is : ")

#     for i in range(1, 11):
#         print(f"{a} X {i} = {a*i}")
# except ValueError:
#     print("Please enter a valid integer.")

# print("Program ended.")

try:
    num = int(input("Enter an integer : "))
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index error occurred.")