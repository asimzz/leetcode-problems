from typing import List

'''
Time complexity: O(n)
Space complexity: O(n)

Where n is the number of elements in the list `nums`.

link: https://leetcode.com/problems/contains-duplicate/description/
'''

def containsDuplicate(nums: List[int]) -> bool:
    seenNums = set()

    for n in nums:
        if n in seenNums:
            return True
        else:
            seenNums.add(n)
    return False


