import random
characters=["#","$","5","%","^","&","8","(",")","_","+","1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","!","@","#"]

pl=int(input("enter the length of your passward"))
passward=""

for i in range(pl):
    passward+=random.choice(characters)
print(passward)