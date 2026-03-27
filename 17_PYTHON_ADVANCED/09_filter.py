num = [1,5,77,96,11,9,6,4,5,6,565,5,5]

def greaterThan9(a):
    if a>9:
        return True
    else:
        return False
    
filtered = list(filter(greaterThan9,num) ) 
print(filtered)  