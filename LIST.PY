a=[10,20,12,10,10,20,19]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)        

n=(int(input("how many num:")))
s=[]
for i in range(n):
    n=int(input("Enter a num:"))
    s.append(n)
print(s)