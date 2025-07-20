class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def longestSequenceandTotalFreq(fd):

            total_freq = 0
            max_freq = 0

            for key in fd:
                total_freq += fd[key]

                if fd[key] > max_freq:
                    max_freq = fd[key]

            return total_freq, max_freq

        max_len = 0

        for i in range(len(s)):

            freq_dict = {}
            freq_dict[s[i]] = 1
            j = i + 1

            while j < len(s):

                if s[j] in freq_dict:
                    freq_dict[s[j]] += 1
                else:
                    freq_dict[s[j]] = 1

                total_freq, max_freq = longestSequenceandTotalFreq(freq_dict)

                if total_freq - max_freq > k:
                    break

                if j - i + 1 > max_len:
                    max_len = j - i + 1

                j += 1

        return max_len

