import datetime
def gettime():
    x=datetime.datetime.now()
    y=str(x)
    return y

work=int(input("enter what you want to do ,1 for get data,2 for lock data "))
# for adding data
if work==2 :
    person=int(input("for whom 1=harry 2=rohan 3=ben"))
    if person==1:
        lock=int(input("what you want to lock, 1=diet,2=exercise "))
        if lock==1:
            with open("harry_diet.txt","a") as f:
                diet=input("what to want to add")

                f.write(gettime())
                f.write(diet +" \n")

        if lock==2:
            with open("harry_exr.txt","a") as f:
                ex=input("what to want to add")

                f.write(gettime())
                f.write(ex +"\n")

    if person == 2:
        lock = int(input("whar you want to lock, 1=diet,2=exercise "))
        if lock == 1:
            with open("rohan_diet.txt", "a") as f:
                diet = input("what to want to add")
                f.write(gettime())
                f.write(diet+ "\n")

        if lock == 2:
            with open("rohan_exr.txt", "a") as f:
                ex = input("what to want to add")
                f.write(gettime())
                f.write(ex + "\n")

    if person == 3:
        lock = int(input("whar you want to lock, 1=diet,2=exercise "))
        if lock == 1:
            with open("ben_diet.txt", "a") as f:
                diet = input("what to want to add")
                f.write(gettime())
                f.write(diet+ "\n")

        if lock == 2:
            with open("ben_exr.txt", "a") as f:
                ex = input("what to want to add")
                f.write(gettime())
                f.write(ex + "\n")

# for getting data

if work==1:
    person = int(input("of whom 1=harry 2=rohan 3=ben"))
    if person==1:
        perf=int(input("which file you want  1=diet,2=exercise "))
        try:
           if perf==1:
             with open("harry_diet.txt") as f :
                print(f.read())
           elif perf==2:
             with open("harry_exr.txt")  as f:
                 print(f.read())
        except:
            print("file does not exist")

    if person == 2:
        perf = int(input("which file you want  1=diet,2=exercise "))
        try:
            if perf == 1:
                with open("rohan_diet.txt") as f:
                    print(f.read())
            elif perf == 2:
                with open("rohan_exr.txt")  as f:
                    print(f.read())
        except:
            print("file does not exist")

    if person == 3:
        perf = int(input("which file you want  1=diet,2=exercise "))
        try:
            if perf == 1:
                with open("ben_diet.txt") as f:
                    print(f.read())
            elif perf == 2:
                with open("ben_exr.txt")  as f:
                    print(f.read())
        except:
            print("file does not exist")
