with open("samrat1.txt") as f :
    print(f.readline())
    print(f.readline())
f=open("samrat1.txt")   #here this fileobject is treated as a different one

print(f.tell())
print(f.readline())