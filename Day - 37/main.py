def func1():    
    try:
        l  = [1, 2, 3]
        i  = int(input("Enter an index: "))
        print(l[i])
    except IndexError:
        print("Index out of range.")
    finally:
        print("Execution completed.")
    
# finally block will always execute, regardless of whether an exception was raised or not. It is typically used for cleanup actions, such as closing files or releasing resources.

if __name__ == "__main__":
    func1()