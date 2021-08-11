# finding Element in an array

def findElement(nums, value):
    nums.sort()
    indexHelper = 0
    while nums:
        size = len(nums)
        if value == nums[size//2]:
            print(f"{value} exists in this array, at index: {indexHelper} *after sorting")
            return
        elif value < nums[size//2]:
            nums = nums[:size//2]
        else:
            nums = nums[size//2 + 1:]
            indexHelper += size // 2 + 1

    print(f"{value} DOESN'T exist in this array")


def anotherway(nums, value):
    if value in nums:
        print(f"{value} exists in this array, at index: {nums.index(value)}")
        return
    print(f"{value} doesn't exist in this array")
    return


findElement([1, 2, 3, 4, 5, 6, 67,1, 0], 4)
anotherway([1, 2, 3, 4, 5, 6, 67,1, 0], 4)
