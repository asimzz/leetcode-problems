from typing import List

'''
Time complexity: O(nlogn)
Space complexity: O(n)

Where n is the number of elements in the list `nums`.
'''

def majorityElement(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    mid = len(sorted_nums) // 2 
    return sorted_nums[mid]