'''
if error in try-except run-
if no error in try-except will not run-else run
either try run or except run -fianlly will always run

'''

f=open("samrat.txt")
try:
    # f=open("samrat2.txt") #tis fill not exist
    f=open("polymorphism") #this file exist
except Exception as e:
    print(e)

else:
    print("except is not running")

finally:
    f.close()
    print("finally will run always")