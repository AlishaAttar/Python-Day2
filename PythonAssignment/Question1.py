#Write a program to read a file and count how many vowels are present in the content
f=open("PythonAssignment/file.txt","r") 
data=f.read()
count=0
for i in data:
        if i in "aeiouAEIOU":
            count+=1
print("Number of vowels",count)
f.close()