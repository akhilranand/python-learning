'''
rec(n) =>    0  1  1  2  3  5  8  13 
      n=>    0  1  2  3  4  5  6  7 
'''
def rec(n):
    if(n==0 or n ==1):
        return n
    return rec(n-2)+rec(n-1)

print(rec(6))