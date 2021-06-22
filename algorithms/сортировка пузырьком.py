arr = [1,7,6,3,4,5,67,812,3]
print(arr)
for i in range(len(arr)):
    for j in range (len(arr)-i-1):
        if arr[j+1]>arr[j]:
            arr[j],arr[j+1]= arr[j+1],arr[j]
print(arr)