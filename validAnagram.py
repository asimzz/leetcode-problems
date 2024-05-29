
'''
Time complexity: O(nlogn)
Space complexity: O(n)

Where n is the length of the strings `s` and `t`.
'''
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)