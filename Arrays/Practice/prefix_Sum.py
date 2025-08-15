arr=[1,24,56,78,85,85,7,79]
pre=[0]*(len(arr))
pre[0]=arr[0]
for i in range(1,len(arr)-1):
    pre[i]=arr[i]+pre[i-1]
print(pre)
