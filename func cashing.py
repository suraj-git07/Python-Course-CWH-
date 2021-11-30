# func-cashing is done to store some results of func (which takes high times)
# let i have a func which takes some time do some task
import time
from functools import lru_cache

@lru_cache(maxsize=1)  #maxsize=no of results saved  ,mor ethe maxsize ,more memory it takes
def somework(n):
   time.sleep(n)
   return n

if __name__ == '__main__':
    print("work start")
    somework(3)
    print("work restart")

    somework(3)    #this time it does not take 3 sec since it already has the result of n=3
    print("work done")
    # now whenever i put n=3 it takes time to run the result
    # by func cashing i cn store the result of n=3 or any other