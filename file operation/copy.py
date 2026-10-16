f = open("file operation/sample.txt", "r")
data = f.read()
f.close()

f = open("new.txt", "w")
f.write(data)
f.close()

print("File copied successfully")