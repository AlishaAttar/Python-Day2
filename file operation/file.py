f = open("file operation/sample.txt", "r")
data = f.read()
words = data.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
print("Length:", len(longest))

f.close()