
#Bubble sort

#worst complexity : O( n^2)
#average complexity : O(n^2)
#best complexity : O(n)
#space complexity : O(1)
#Method: Exchanging
#Class : comparison sort


def bubbleS(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

            else:
                pass

    return arr

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    new_arr = bubbleS(arr)

    print(arr)
