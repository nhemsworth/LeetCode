"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Beats 52.60% on execution time
Beats 81.71% on memory usage
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = j = len(s) - 1
        # Find the end of the last word
        while i >= 0 and s[i]==" ":
            i -= 1
            j -= 1

        # Find the beginning of the last word
        while i >= 0 and s[i]!=" ":
            i -= 1

        # Return difference of the two pointers
        return j - i