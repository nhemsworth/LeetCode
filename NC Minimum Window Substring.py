class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def create_freq_dict(st):
            fd = {}
            for char in st:
                if char in fd:
                    fd[char] += 1
                else:
                    fd[char] = 1
            return fd

        def remove_elem(key, dt):
            if dt[key] > 1:
                dt[key] -= 1
            else:
                dt.pop(key)
            return dt

        def add_elem(key, dt):
            if key in dt:
                dt[key] += 1
            else:
                dt[key] = 1
            return dt

        i = 0
        j = 0
        shortest_str = s
        str_dict = create_freq_dict(t)
        missing_dict = create_freq_dict(t)
        valid_substr_found = False

        if len(t) > len(s):
            return ""

        # First, increase left index to first
        while i < len(s) and s[i] not in str_dict:
            i += 1

        # If we get to the end without finding a char, we return an emtpy string
        if i == len(s):
            return ""

        # Remove first missing element
        missing_dict = remove_elem(s[i], missing_dict)
        j = i + 1
        while j < len(s) and missing_dict == True:

            if s[j] in missing_dict:
                missing_dict = remove_elem(s[j], missing_dict)

            j += 1

        if j == len(s) and missing_dict == False:
            return s[i: j + 1]
        elif j == len(s):
            return ""

        shortest_str = s[i: j + 1]

        while j < len(s):

            if missing_dict == False and s[i] in str_dict:
                if len(s[i: j + 1]) < len(shortest_str):
                    shortest_str = s[i: j + 1]

                missing_dict = add_elem(s[i], missing_dict)
                i += 1

            elif missing_dict == False:
                i += 1
            elif s[j] in str_dict:
                missing_dict = remove_elem(s[j], missing_dict)
                j += 1
            else:
                j += 1

        return shortest_str



























