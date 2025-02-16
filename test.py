from typing import List

def max_ascending_sum(nums: List[int]) -> int:
    
    sum_of_ascend = nums[0]

    for x in range(1, len(nums)):
        if nums[x-1] < nums[x]:
            sum_of_ascend += nums[x]
        else:
            sum_of_ascend = 0
            sum_of_ascend += nums[x]

    return sum_of_ascend


nums = [10,20,30,5,10,50]
print("Hello world!")

max_ascending_sum(nums)