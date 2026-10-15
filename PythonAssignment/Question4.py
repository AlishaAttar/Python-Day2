
f = open("PythonAssignment/file.txt", "r")
data = f.read()
words = data.split()
print("Total number of words:", len(words))
unique = []
for i in words:
    if i not in unique:
        unique.append(i)
print("Unique words:", unique)
f.close()
