def search(a,key):
    for x in a:
        if key in a:
            print("found")
        else:
            print("not found")
    return search
print(search([10,20,30],30))          