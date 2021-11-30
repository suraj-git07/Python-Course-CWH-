file= open("samrat1.txt","r")
# a=file.read()
# print(a)
# b= file.read(34)    #here n inside r is bytes
# print(b)

# if the value of byte is greater than the limit is print the whole content
# it only read file once(complete)
c=file.readline()
print(c)

# d= file.readlines()  #it sores each line as a element of list
# print(d)  # see output


# file  already has a \n sequency at the end of each line
file.close()