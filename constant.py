#Run this code and you should see that as the number of elements
#in the array increases, the time taken to add to it remains constant

import time

#measure time taken to add to small array
start_time = time.time()

array1 = [3,1,4]

array1.append(1)
    
print("\n%s seconds" % (time.time() - start_time))


#measure time taken to add to slightly larger array
start_time = time.time()

array2 = [3,1,4,1,5,9,2]

array2.append(6)
    
print("\n%s seconds" % (time.time() - start_time))


#measure time taken to add to even larger array
start_time = time.time()

array3 = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]

array3.append(3)
    
print("\n%s seconds" % (time.time() - start_time))
