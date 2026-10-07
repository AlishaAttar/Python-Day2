text="  welcome to IMCC!"
print("Add spaces",text.strip()) #removes spaces from both ends

print("Lower case:",text.lower()) #converts into lower case
print("upper case:",text.upper())#conerts into upper case
print("Capitalize first letter:",text.capitalize())
print("title case",text.title())#capitalize each word
print("Letter c occurs",text.count("C"),"times in text")#findds number of times it occured in the string
print("Posiion of imcc is",text.find("IMCC"))#givs position
print(text.replace("IMCC","Python")) #takes 2 parameters one to replace and one to add
print(text.startswith("  WE"))# gives boolean value
print(text.endswith("!"))
print(text.split())
words=["python","is","fun"]
print(" ".join(words))
txt="ha"
print(txt*3)
#accept a string and count the vowels 

str="hehe"
print(txt+str)

#Length
numbers=[1,2,3,4,5,6,7,8,9]
print("no od items in list are:",len(numbers))
#sum
print(sum(numbers))
#sorting
print(sorted(numbers))
print(sorted(numbers,reverse=True))



