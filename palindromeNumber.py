
'''
Time complexity: O(n)
Space complexity: O(n)

Where n is the number of digits in the integer `x`.

link: https://leetcode.com/problems/palindrome-number/description/
'''
def isPalindrome(x: int) -> bool:
    return str(x)[::-1] == str(x)