from typing import List

'''
Time complexity: O(n.klogk)
Space complexity: O(n)

Where n is the number of strings in the list `strs`, and k is the average length of the strings.
'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams_map = {}

    for i,s in enumerate(strs):
        sorted_s = "".join(sorted(s))
        if sorted_s in anagrams_map:
            anagrams_map[sorted_s].append(s)
        else:
            anagrams_map[sorted_s] = [s]
    return anagrams_map.values()