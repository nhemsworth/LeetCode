
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best_length = 0
        D = set()

        i = 0
        j = 0
        while j < len(s):

            if s[j] not in D:
                D.add(s[j])
                j += 1
            elif i < j:
                if j- i > best_length:
                    best_length = j - i
                D.remove(s[i])
                i += 1
            else:
                D.remove(s[i])
                j += 1

        if j - i > best_length:
            return j - i
        else:
            return best_length

# Beats 76.50% on execution time
# Beats 96.14% on memory usage
