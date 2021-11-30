# corountines is just like we cashed some part of program and  do some work after that part
import time

def  searcher():
    with open("samrat.txt") as f:
        data=f.read()

        time.sleep(4)     #let it take 4 sec to read it
    while True:
        text=(yield)    #take text on the go

        if text in data:
                print("your text in data")
        else:
                print("sorry text not in data")


#now searcher is not only a func but also a corountine
# creating instance for it

search=searcher()
#applying next to read the file
next(search)
#for giving text
search.send("samrat")
# now it doesn't take those 4 secs
input("enter something")    #just to show time diff
search.send("samrat")
#not only for samrat for any text