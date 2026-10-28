with open("file handling/new.txt","r") as f:
    data=f.read()
print(data)
for line in f:
    print(line,end="")

