import numpy as np


# # ways to crete arrays
myarry = np.array([1, 2, 3], np.int8)
#
# zeroes = np.zeros((2,5), int)    #input is bacially a shape for arry  and output is arry of zeroes with the inputted str
#
# rng = np.arange(15)       # output arrray where element is according to the range input
#
# lins = np.linspace(0, 10, 5,)      # first input : start  , sec input: stop , third  input: no of elements
#
# emp = np.empty((1,4))   #filled with random elements acc to shape
#
# emp_like = np.empty_like(myarry)   #copy shape of myarry and give empty array acc to that
#
# identity = np.identity(10)         #return array of 10 by 10
#

# for getting the dimensions
# print(myarry.shape)


# for getting data type
# print(myarry.dtype)

# for getting total no of elements
# print(myarry.size)

# for reshaping

# rng = rng.reshape(3,5)       #here rng initial shape = 1,15   total elements 15 , after reshaping shape = 3,5  elements still 15
#
# print(rng)
#
# # for reshaping to 1D array
#
# rng = rng.ravel()
#
# print(rng)


# axis
# in 2D Arrays Axis 0 is towards row and Axis1 is towards column
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr = np.array(x)

# print(arr.sum())  #sumall
# print(arr.sum(axis= 0))  # returns an array by doing sum according to axis given
# print(arr.sum(axis= 1))  # returns an array by doing sum according to axis given
# print(arr.T) #transpose the array
# print(arr.flat)         #returns an iterator
# print(arr.nbytes)        #returns the no of total bytes consumed


# print(arr.ndim)            #returns dimensions
# for i in arr.flat :
#     print(i)               #see output


###for 1D   for 2D it also take axis
# for getting pos of max ele
# print(arr.argmax())

# for getting pos of min ele
# print(arr.argmin())


# for getting the sequence of pos by which array become sorted
# print(myarry.argsort())

