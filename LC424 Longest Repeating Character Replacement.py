"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times. Return the length of the longest substring
containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        j = 0
        longest_str = 0
        freq = {}

        while i < len(s) and j < len(s):

            # Determining the frequency of the maximum element
            max_freq = 0
            max_key = [s[i]]
            if len(freq) != 0:
                for key in freq:
                    if freq[key] > max_freq:
                        max_freq = freq[key]
                        max_key = [key]
                    elif freq[key] == max_freq:
                        max_key.append(key)

            if j < len(s) and ((j - i - max_freq < k) or s[j] in max_key):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1
                j += 1

            else:
                freq[s[i]] -= 1
                i += 1

            longest_str = max(longest_str, j - i)

        return longest_str


sol = Solution()
s = "ABCCCCC"
k = 2
print(sol.characterReplacement(s, k))
