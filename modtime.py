import time
# to find the execution time of a for loop
# initial =time.time()  #it gives me tiks
# for i in range(45):
#     print("samrat is best")
# time_taken=time.time()-initial
# print(f"time taken is {time_taken}")

# to print the curren tiume with date
print(time.asctime(time.localtime(time.time()))) # here time.time() gives  me tik,time.localtime() canges this in a tuple, time.asctime() changes it in a str

# sleep func
# tmie.sleep is use for wait while running the prog
# for i in range(4):
#  print("hello")
#  time.sleep(2)