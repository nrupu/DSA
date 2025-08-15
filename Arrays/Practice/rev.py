arr=[1,24,56,78,85,85,7,79]
i,r=0,len(arr)-1
while i<r:
    arr[i],arr[r]=arr[r],arr[i]
    i+=1
    r-=1
print(arr)
