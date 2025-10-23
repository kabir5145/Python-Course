# String Methods in python

# Strings are immutable

a= "! !kabir!! !! !"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.replace("a","f"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str_1 = "Welcome to the console !!!"
print(str_1.center(50))

print(a.count("kabir"))

print(str_1.endswith("to",4,10))

str1 = "He's name is Dan . He is an honest man."
print(str1.find("is"))
# print(str1.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "We wish you a Merry Cristmas"
print(str1.isprintable())

str_2 = "      "    
print(str_2.isspace())

str_1 = "World Health Organisation"
print(str_1.istitle())