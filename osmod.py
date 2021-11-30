import os    #built in  module
# to show methods
print(dir(os))

# to show current working dir    cwd is the place where my porg considered the files
# print(os.getcwd())

# chainge cwd
# os.chdir("c://")
# print(os.getcwd())   #so my cwd is changed


# to list files
print(os.listdir())   #it gives result in type of list


# to make folder at cwd
# os.mkdir("this")  #this =name

# to make multiplefolders
# os.makedirs("this/that")   #this is folder,that is sub folder

# to rename a file
# os.rename("samrat.txt","samrat1.txt")

# to read envirnment variable
# print(os.environ.get("Path"))
#
# # path join to join to paths
# os.path.join()

# to check the existance of path(dir)
# print(os.path.exists("samrat"))
#
# # to check the existance of file
#
# print(os.path.isfile("samrat1.txt"))
