def remove_element(nums, val=0):
    for i in range(len(nums)):
        if nums[i] == val:
            nums.append('_')
    while val in nums:
        nums.remove(val)
    return nums


print(remove_element([1, 2, 3, 3, 3, 4, 5], 3))
