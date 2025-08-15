#left rotation
arr=[1,24,56,78,85,85,7,79]
arr = arr[1:]+arr[:1]
print(arr)
#right rotataion
arr=[1,24,56,78,85,85,7,79]
arr=arr[-1:]+arr[:-1]
print(arr)
