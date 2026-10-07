list=[1,2,3,4,5,6,7,8,9,0]
print("Sum of last 4 digits" ,sum(list[-4:]))

print("Removed items at second and fifth position" ,list.remove(2),list.remove(5),list)

l1=max(list)
l2=min(list)
print("the difference between smallest and largest no of string :",l1-l2 )


new_list=list[2]/2
list.append(new_list)
print(list)