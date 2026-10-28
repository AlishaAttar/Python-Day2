def count_v(s):
    count=0
    for ch in s.lower():
        if ch in "aeiou":
            count+=1
    return count
print(count_v("Hello"))    