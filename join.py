lis=["iron","man","captain","america","hulk","thor","odinson"]
# let i have to print the items of list with and b/w in items
# first way
for i in lis:
    print(f"{i} and ",end=" ")
print()
# join way
a=" and ".join(lis)   #format- waht thar have to join .join(jisme loop chalega)
print(a)