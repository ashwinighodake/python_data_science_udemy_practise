# Numpy is python library for creating N-Dimensional array, built in linaer algebra.
import numpy as np

arr=[1,2,3]
np.array(arr)
print(arr)

arr=np.arange(0,25)  # creating list 0-25 number
print(arr)

arr=arr.reshape(5,5) #reshaping
print(arr)

ranarr=np.random.rand(5)
print("random array gets created: ",ranarr)

ranarr=np.random.randint(0,101,5)
print("random array gets created: ",ranarr)


max=ranarr.max()
print("max value in the random array is:",max)

max_location=ranarr.argmax()
print("max location",max_location)


min=ranarr.min()
print("min : ",min)

min_location=ranarr.argmin()
print("min location: ",min_location)

identity_mat=np.eye(5)
print("identity matrix:",identity_mat)

one_mat=np.ones(5)
print("one matrix:",one_mat)

#one_mat=np.ones(5,5)
#print("ones mat",one_mat)

zero_mat=np.zeros(5)
print("zeros mat",zero_mat)

arr_linspace=np.linspace(0,10,12)
print("linspace array:",arr_linspace)

arr=np.arange(0,25).reshape(5,5)
print(arr)

row_sum=arr.sum(axis=0)
print("Rows addition:",row_sum)

col_sum=arr.sum(axis=1)
print("column addition:",col_sum)