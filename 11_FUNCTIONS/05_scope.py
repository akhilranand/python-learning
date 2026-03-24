gData = 10 #global scope
gData1 = 23
def sun(a,b):
    c = a+b
    d = 5 #local scope
    gData = 100
    global gData1 #can be changed everywhere
    gData1 = 55
    print(c)

sun(5,2)    
print(gData)
print(gData1)

#print(d) # will give an error because its local scope 