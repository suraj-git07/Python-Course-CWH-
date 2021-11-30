
import random
a=0
userwin=0
compwin=0
while a<=10:
    user = input("enter what you want to do,s=stone,p=paper,sr=sissors")
    try:

      if user == "s":
        user = "stone"
      elif user == "p":
        user = "paper"
      else:
        user = "sissors"
      computer=random.choice(["stone","paper","sissors"])
      if user=="stone" and computer=="paper":
        compwin+=1
        print("user lose")
      elif user=="stone" and computer=="stone":
        pass
        print("draw")
      elif user=="stone" and computer=="sissors":
        userwin+=1
        print("user win")
      elif user=="paper" and computer=="sissors":
        compwin+=1
        print("user lose")
      elif user=="paper" and computer=="paper":
        pass
        print("draw")
      elif user=="paper" and computer=="stone":
        userwin+=1
        print("user win")
      elif user=="sissors" and computer=="stone":
        compwin+=1
        print("user lose")
      elif user=="sissors" and computer=="sissors":
        pass
        print("draws")
      else:
        userwin+=1
        print("user win")
      print(f"user={userwin},computer={compwin}")

      a+=1
    except:
      print("sorry i didn't got it")

if userwin>compwin:
    print("cong user you are the winner")
    print(f"user points :{userwin},computer points:{compwin}")
elif userwin<compwin:
    print("sorry user you lose")
    print(f"user points:{userwin},computer points:{compwin}")
else:
    print("match draws")