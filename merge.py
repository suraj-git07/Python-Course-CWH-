#Merge sort is a divide and conquer Algorithm.

#time complexity: O(nlog n)
#space complexity: O(n)

def mergeSort(arr):

    print("Splitting ", arr)
    if len(arr)>1:

        
 
        mid = len(arr)//2  # finding the mid of arr
        l = arr[:mid] #divide the arr ele
        r = arr[mid:] # into two halves

        mergeSort(l) #sorting the fist half
        mergeSort(r)  #sorting the second half

        #now merging

        i=j=k=0

        while i< len(l) and j < len(r):
            if l[i] < r[j]:
               arr[k] = l[i]
               i+=1

            else:
                arr[k] = r[j]
                j+=1

            k+=1

        #checking if any element was left

        while i< len(l):
             arr[k] = l[i]
             i+=1
             k+=1
         
        while j< len(r):
             arr[k] = r[j]
             j+=1
             k+=1

    print("Merging " , arr)


if __name__ == "__main__":
    

    arr = [5,4,3,2,1]

    mergeSort(arr)

    print(arr)
            
