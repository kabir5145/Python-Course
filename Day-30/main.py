# factorial(7) = 7*6*5*4*3*2*1

def factorial(n):
    if n ==1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

# fibonacci(7) = 0,1,1,2,3,5,8

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))