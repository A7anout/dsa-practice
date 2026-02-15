#solution 1: symmetric
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s) - 1
        for i in range(len(s)):
            if s[i] == '(' and s[n-i] != ')' or s[i] == '{' and s[n-i] != '}' or s[i] == '[' and s[n-i] != ']':
                return False
            return True
"""
Time Complexity: O(n)
Space Complexity: O(1)
this solution is not working for all cases 
because it requires symmetric list
example: works on ({[]}) not on (){}[] 
"""
#solution 2: stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '('
                    , ']'  : '['
                    , '}'  : '{'
                      } # why closed then open? because the stack is lifo
        for c in s: #c stands for character. aka each parentheses
            if c in closeToOpen:    
                if stack and stack[-1] == closeToOpen[c]: #if stack insures the stack is not empty. stack[-1] means last pushed element (the top of the stack).
                    stack.pop()
                else: 
                    return False
            else: # this is an open parentheses so we push
                stack.append(c)
        return True if not stack else False #can be shorthanded to: return not stack
"""
Time Complexity: O(n)
Space Complexity: O(n)
explaination:
the idea is for each open parentheses. the closed parentheses of closes the latest open one of same type
example: ((). the closing one closes the second open one not the first
so we go throgh the given string.
what if the first is closed not open? then the string must be invalid. ex: )(){}[] 
we start with pushing the parentheses into the stack
if a parentheses is open, we push it into the stack
    if the next parentheses is closing of same type. we pop the open one inside the stack. ex: ()
    if the next parentheses opening of same type. we also push (()
    if the next parentheses is opening of diffrent type. we push. ex: ([])
    if the next parentheses is closing of diffrent type. then the string is invalid ex: (])
in summary: if its open. push
if closed. pop the open (must be same type)
example: ([{}])
the stack starts with: (
next parentheses [ is open then we push
stack now contains ([
next parentheses { is open then we push
stack now contains ([{
next parentheses } is closed then we pop
stack now contains ([
next parentheses ] is closed then we pop
stack now contains (
next parentheses ) is closed then we pop
stack now is empty
once we are irretating through the given string we check the stack
if it's empty (if not stack) then the string was valid
if not return invalid
"""