from typing import List

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_dicts = []

        for entry in strs:
            entry_dict = {}
            for c in entry:
                if c in entry_dict:
                    entry_dict[c] += 1
                else:
                    entry_dict[c] = 1
            str_dicts.append(entry_dict)

        output = []

        while str_dicts:
            matches = []
            match_idx = [0]
            # Collecting match indices throughout list
            for i in range(1, len(str_dicts)):
                if str_dicts[0] == str_dicts[i]:
                    match_idx.append(i)

            # Collecting matching strings
            for i in range(len(match_idx)):
                matches.append(strs[match_idx[i]])

            output.append(matches)

            new_strs = []
            new_str_dicts = []
            for i in range(len(str_dicts)):
                if i not in match_idx:
                    new_strs.append(strs[i])
                    new_str_dicts.append(str_dicts[i])
            str_dicts = new_str_dicts
            strs = new_strs

        return output



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution1()
output = sol.groupAnagrams(strs)

print(output)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Beats 65.84% on execution time
        # Beats 68.69% on memory usage
        str_map = {}

        for entry in strs:
            entry_sorted = str(sorted(entry))
            if entry_sorted in str_map:
                str_map[entry_sorted].append(entry)
            else:
                str_map[entry_sorted] = [entry]

        result = []
        for key in str_map:
            result.append(str_map[key])

        return result

sol = Solution()
output = sol.groupAnagrams(strs)

print(output)



