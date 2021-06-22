nums = [12,56,876,1234,876,123,54,3,5]
print(nums)
nums.sort()
print(nums)

search_for = int(input("Какое число ищем ? >>"))
lowest = 0
highest = len(nums)-1
index = None

while (lowest<=highest) and (index is None):
    mid = (lowest+highest)//2

    if nums[mid] == search_for:
        index = mid

    else:
        if search_for < nums[mid]:
            highest = mid -1
        else:
            if search_for > nums[mid]:
                lowest = mid + 1
print("Искомый элемент",search_for,"Находится под индексом",index)