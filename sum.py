num=int(input("Enter your num:"))
sum=0

while(num>0):
        
        sum +=num%10
        num=num//10
print("output:",sum)
