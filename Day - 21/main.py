# def average(a,b):
#     print("The average is ", (a+b)/2)
# average(4,6)

def average(*numbers):
    print(type(numbers))
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return avg

print("The average is ", average(2,3,4,5,6,7,8,9))


# def name(**name):
#     print(type(name))
#     print("Hello,", name["frame"],name["mname"], name["lname"])
    
# name(mname="Steve", lname="Rogers", frame="Captain")

