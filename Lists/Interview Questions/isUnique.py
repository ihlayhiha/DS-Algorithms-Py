# check if all elements in the list are unique

def isUnique(nums):

    nums.sort()
    while nums[0] != nums[-1] and nums.pop() != nums[-1]:
        pass
    else:
        if len(nums) == 1:
            print("Yes! This list is Unique!")
            return
        print("This list is not unique")


    # empty = []
    # for value in nums:
    #     if value in empty:
    #         print('This list is not unique')
    #         return
    #     empty.append(value)
    # print("Yes this list is Unique")


myList = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 13, 14, 35, 16, 27, 58, 19, 21, 70, 70]

isUnique(myList)