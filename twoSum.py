from typing import List

'''
Time complexity: O(n)
Space complexity: O(n)

Where n is the number of elements in the list `nums`.

link: https://leetcode.com/problems/two-sum/description/
'''

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        else:
            prevMap[n] = i
    return

'''
BruteForce Solution:

Time complexity: O(n^2)
Space complexity: O(1)

Where n is the number of elements in the list `nums`.
'''
def twoSum(nums: List[int], target: int) -> List[int]:
    N = len(nums)
    for i in range(N-1):
        for j in range(i+1, N):
            numsSum = nums[i] + nums[j]
            if numsSum == target:
                return [i,j]