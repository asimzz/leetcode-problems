
'''
Time complexity: O(n)
Space complexity: O(n)

Where n is the length of the string `s`.

link: https://leetcode.com/problems/roman-to-integer/description/
'''

def romanToInt(s: str) -> int:
    roman_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = list(s)[::-1]
    prev = roman_nums[number[0]]
    result = prev
    for num in number[1:]:
        curr = roman_nums[num]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result