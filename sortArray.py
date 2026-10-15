arr = [1, 2, 3, 4, 5]

def sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i]+1:
            return False
        return True
print(sort(arr))    