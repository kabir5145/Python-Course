dic = {
    "Harry":"Human Being",
    69 : "Number"
}
# print(dic["Harry"])
# print(dic[69])

# for key in dic.keys():
#     print(dic[key])

print(dic.items())
for key, value in dic.items():
    print(f"Key is {key} and value is {value}")