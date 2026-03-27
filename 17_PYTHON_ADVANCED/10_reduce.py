from functools import reduce

num = [1,5,77,96,11,9,6,4,5,6,565,5,5]

def sum(a,b):
    return a+b

added = reduce(sum,num)

print(added)