# My solution which works
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""

        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack = stack + bracket
            elif bracket == ")" and len(stack)>0:
                if stack[-1] == "(":
                    stack = stack[:-1]
                else:
                    return False
            elif bracket == "}" and len(stack)>0:
                if stack[-1] == "{":
                    stack = stack[:-1]
                else:
                    return False
            elif bracket == "]" and len(stack)>0:
                if stack[-1] == "[":
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False

        return len(stack) == 0

# Nice solution in the comments. I like that they can use the pop() function since they're using a list.
class Solution2(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false