#Run this code and you should see that as the number of elements
#in the array increases, the time taken to traverse it increases

import time

#measure time taken to traverse small array
start_time = time.time()

array1 = [3,1,4]

for num in array1:
    print(num)
    
print("\n%s seconds" % (time.time() - start_time))


#measure time taken to traverse slightly larger array
start_time = time.time()

array2 = [3,1,4,1,5,9,2]

for num in array2:
    print(num)
    
print("\n%s seconds" % (time.time() - start_time))


#measure time taken to traverse even larger array
start_time = time.time()

array3 = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]

for num in array3:
    print(num)
    
print("\n%s seconds" % (time.time() - start_time))
