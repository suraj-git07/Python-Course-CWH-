# file =open("samrat.txt","w")#writing methods

# it truncate the existing txt and add new text ,also create file if does not exist
# file.write("samrat is the best")

# now to append new data
# filea=open("samrat.txt","a+")
# filea.write("samrat is the universe \n")
# filea.write("samrat is the coading \n")
#  to check the no of character you print ,store the write func in a variable and just print it
# using writelines
# lines=["samrat is best \n","samrat is ironman\n","samrat loves everyone\n"]
# filea.writelines(lines)
# filea.seek(0)
# s=filea.readlines()
# print(s)

# for read and write both mode
# file=open("samrat.txt","r+")
# a=file.read()
# file.write("samrat loves coading very much")

# print(a)


# file.close