#Run this code and you should see that as the number of elements
#in the array increases, the time taken to sort it increases
#exponentially

import time

#bubble sort code adapted from - https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubbleSort(array):
    n = len(array)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]


#measure time taken to sort small array
start_time = time.time()
  
array = [3,1,4]
  
bubbleSort(array)
  
print ("Sorted array is:")
for i in range(len(array)):
    print ("%d" %array[i]), 

print("\n%s seconds\n" % (time.time() - start_time))


#measure time taken to sort larger array
start_time = time.time()
  
array = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
  
bubbleSort(array)
  
print ("Sorted array is:")
for i in range(len(array)):
    print ("%d" %array[i]), 

print("\n%s seconds\n" % (time.time() - start_time))

