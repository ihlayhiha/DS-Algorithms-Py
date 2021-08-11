# program to find all pairs of integers whose sum is equal to given number


def sumPairs(nums, total):

    # pairs = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == total:
    #             pairs.append((i, j))
    # return pairs

    count = -1
    while True:    
        check = nums.pop()
        for num in nums:
            if num + check == total:
                return count, nums.index(num)
        count -= 1
        

print(sumPairs([3, 2, 4], 6))
