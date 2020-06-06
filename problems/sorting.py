f = open("dictionary.txt","r")

arr = f.readlines()

f.close()

arr.sort()

for pair in arr:
    if pair != "\n":
        print(pair[:len(pair)-1])
