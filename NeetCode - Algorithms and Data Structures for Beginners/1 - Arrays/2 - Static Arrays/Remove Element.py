#solution 1 bruteforce
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tempList = []
        for i in nums:
            if i != val:
                tempList.append(i)
        nums[:] = tempList
        return len(nums)
"""
Time complexity: O(n)
Space complexity: O(n)
the problems asks for in place modification so this is not the best solution.
"""

#solution 2 two pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1
        return L

"""
Time complexity: O(n)
Space complexity: O(1)
example: Input: nums = [1,1,2,3,4], val = 1
we start wit both L and R at index 0 (first 1)
does R value equal val? yes, so we increment R to index 1 (second 1)
L still at index 0
does R value equal val? yes, so we increment R to index 2 (2)
L still at index 0
does R value equal val? no, so we copy value at R value to L and increment both L and R

keep going until R reaches the end of the array
Output: [2,3,4]
we return L which is 3
"""