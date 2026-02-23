ep1 = {
    122 : 45,
    567 : 89,
    670 : 69
}
ep2 = {
    222 : 67,
    566 : 90
}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[567]
print(ep1)