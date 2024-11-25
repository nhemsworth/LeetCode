"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Beats 48.90% in terms of execution time
Beats 42.78% in terms of memory usage
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nlen = len(needle)

        for i in range(len(haystack) - nlen + 1):
            if haystack[i:i + nlen] == needle:
                return i

        return -1
