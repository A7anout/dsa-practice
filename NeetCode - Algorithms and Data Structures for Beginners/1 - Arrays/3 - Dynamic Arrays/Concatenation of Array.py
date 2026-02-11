#solution 1: simple?
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

"""
Time Complexity: O(n)
even tho we didn't explicitly use a loop,
the concatenation operation internally iterates through the list to create a new list.
Space Complexity: O(n)
A new list of size 2n is created
the solution isn't best in this chapter as we should be using dynamic array features
"""

#solution 2: creating a refrence
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans.extend(nums)
        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n) (the array is expanded by 2)
this is wrong because ans is a refrence to nums, so we are not creating a new list.
this modifies the original list, which is not allowed.
"""

#solution 3: Manual append
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
"""
time complexity: O(n)
space complexity: O(n)
"""


