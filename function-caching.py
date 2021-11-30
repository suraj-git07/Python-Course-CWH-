# function caching is used to save some(depend on user input) return values of func
# for ex
import time

#
# def some_work(n):
#     time.sleep(n)    #this is for making a  case , where a func do calculation and return a value , take n sec
#     return n
#
#
# if __name__=="__main__":
#     some_work(3)
#     print("calling again..")
#     some_work(3)     #doing the same work
#     print("called again")
#     #it also take 3 secs  but to save time we can do


from functools import lru_cache    #lru_cache for caching


@lru_cache(maxsize=3)    #maxsize=latest n values to cache
def some_work(n):
    time.sleep(n)    #this is for making a  case , where a func do calculation and return a value , take n sec
    return n


if __name__=="__main__":
    some_work(3)
    print("calling again...")
    some_work(3)     #doing the same work
    print("called again")
    #this time it doesn't take 3 sec becaue the return value is cached above
