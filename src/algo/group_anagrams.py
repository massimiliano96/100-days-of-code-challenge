# Given an array of strings 'strs' group the anagrams together
""" 
Example : 
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["tan", "nat"], ["ate", "eat", "tea]]
"""

from collections import defaultdict


def group_anagrams(strs):
    ans = defaultdict(list)

    for word in strs:
        key = [0] * 26

        for letter in word:
            key[ord(letter) - ord("a")] += 1

        key = tuple(key)

        ans[key].append(word)

    return ans
