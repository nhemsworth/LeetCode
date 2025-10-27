class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        num_content = 0
        g_i = 0
        s_i = 0

        while g_i < len(g) and s_i < len(s):

            if s[s_i] >= g[g_i]:
                num_content += 1
                s_i += 1
                g_i += 1
            else:
                s_i += 1

        return num_content