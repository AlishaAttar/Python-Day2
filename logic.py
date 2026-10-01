n=int(input("Enter a number :"))
count=0
for i in range(n):
    if n ==0:
      break
    n=n//10
    count+=1
    print(count)
   