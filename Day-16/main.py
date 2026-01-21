x = int(input("Enter the value of x:"))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x < 0:
        print(x)
    case _ if x % 2 == 0:
        print("x is even")
    case _ if x % 2 != 0:
        print("x is odd")