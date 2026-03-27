def add(*arg):
    total = 0
    for i in arg:
        total+=i
    return total


print(add(1,3,5))