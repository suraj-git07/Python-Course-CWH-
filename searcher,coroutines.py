def searcher():
    import time
    #some book is reading

    book="hello ,hi ,bye bye"
    time.sleep(3)                          #this is running only one time after every call, this concept in coroutines

    while True:
        text=(yield)
        if text in book:
            print("text is in the book")
        else:
            print("text is not in the book")

search=searcher()
next(search)
# search.send("h")
text=input("press any key")
search.send(text)
