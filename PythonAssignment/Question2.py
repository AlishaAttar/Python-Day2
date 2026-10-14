#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

f = open("PythonAssignment/file.txt", "r")

lines = f.readlines()

print("Total number of lines:", len(lines))
print("Second line:", lines[1])
print("Fourth line:", lines[3])

f.close()
