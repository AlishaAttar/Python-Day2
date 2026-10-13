
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial    
n=int(input("Enter the value of n:"))
print(fact(n))