import numpy #numpy is a mdoule in Python
arr = numpy.array(42) #0D array
arr2 = numpy.array([1,2,3,4,5,6,7]) #1D array
arr3 = numpy.array([[1,2,3,4,5], [6,7,8,9,10]]) #2D array
arr4 = numpy.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]]) #3D array
print(arr.ndim) #'.ndim' checks how many dimensions an array has
print(numpy.__version__) #prints out your current numpy version
print(type(arr)) #prints out the type of array
print(arr2[0]) #access array elements
print(arr3[0,1]) #we use comma seperated integers representing dimension and index of element to access elements in 2D array
print(arr4[0,1,2]) #same instruction from above to access 3D elements
print(arr3[1,-1]) #use negative indexing to access an array from the end 
print(arr2[1:5]) #slice an array using a colon inside of the square brackets [start:end]
print(arr2[1:5:2]) #use step value to determine the step of the slicing [start:end:step]
print(arr3[1,1:4]) #slicing 2D array. this example slicing from second element exclude 1-4
print(arr3[0:2,2]) #slices from both elements and returns index 2
print(arr3.shape) #shows the shape of an array
#data types: 
    #i - integer
    #b - boolean
    #u - unsigned integer
    #f - float
    #c - complex float
    #m - timedelta
    #M - datetime
    #O - object
    #S - string
    #U - unicode string
    #V - fixed chunk of memory for other type ( void )
print(arr2.dtype) #checks the data type of an array
arr5 = numpy.array([1,2,3,4,5], dtype="S") #create an array with a defined data type
print(arr5)
#best way to change the data type of existing array is to make a copy with astype() method:
a = numpy.array([1.1,2.1,3.1,4.1])
newarr = a.astype("i")
print(newarr)
newarr = a.astype(int) #change data type from float to integer using 'int'.
print(newarr)
#'.copy()' and '.view()' allow you to copy or view an array
b = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
newb= b.reshape(4,3) #reshape a 1D array into a 2D array, uses '.reshape' function, 4 arrays/3 elements
print(newb)
c = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])