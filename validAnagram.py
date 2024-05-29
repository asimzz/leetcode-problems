
'''
Time complexity: O(nlogn)
Space complexity: O(n)

Where n is the length of the strings `s` and `t`.

link: https://leetcode.com/problems/valid-anagram/description/
'''
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)