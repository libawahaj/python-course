#arrays

import array as arr

#setting up an array

array_num = arr.array('i', [1,2,3,4,3,5,6,3,7])
print("The original array is ", array_num)

#counting the frequency in an array

count = array_num.count(3)
print("The number of times '3' appears in this array is ", count)

#reversing an array

reversed = array_num.reverse()
print("The reverse of this array is: ", array_num)