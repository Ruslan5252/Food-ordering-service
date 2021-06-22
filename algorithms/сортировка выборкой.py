arr = [3,2,1]

print("Было",arr)

for i in range(len(arr)):
    lowest = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[lowest]:
            lowest = j
    arr[i],arr[lowest] = arr[lowest],arr[i]
print("Стало",arr)
