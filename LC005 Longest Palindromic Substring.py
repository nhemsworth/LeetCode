
class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_substring = ""

        for c in range(len(s)):

            l = r = c
            working = True
            while working:
                # s[l:r+1] == s[l:r+1][::-1]:

                if r - l + 1 > len(longest_substring):
                    longest_substring = s[l: r + 1]

                if l > 0 and r < len(s)-1:
                    if s[l-1: r+2] == s[l-1: r +2][::-1]:
                        l -= 1
                        r += 1
                    elif s[l: r+2] == s[l: r +2][::-1]:
                        r += 1
                    else:
                        working = False
                        break

                elif r < len(s) - 1:
                    if s[l: r+2] == s[l: r + 2][::-1]:
                        r += 1
                    else:
                        working = False
                        break

                else:
                    working = False
                    break

        return longest_substring

sol = Solution()
s = "abba"
out = sol.longestPalindrome(s)
print(out)