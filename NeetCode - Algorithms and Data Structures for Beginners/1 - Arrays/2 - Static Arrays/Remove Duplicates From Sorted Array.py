# solution 1 brute force in place
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
"""
Time complexity: O(n²)
Space complexity: O(1)
Why this doesn't work in this chapter: it depends on lists being dynamic array.
Why O(n²): pop takes O(n) to shift all elements to the left.
worst case we call pop for all elements (n) times
Why not increment i after nums.pop(i). because index i now holds 
the next element after the one we popped so that would skip the next element.
"""
# solution 2 set
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums[:]))
        return len(nums)
"""
Time complexity: O(nLogn) (n for set, nLogn for sorting) 
Space complexity: O(n) because set takes O(n) space
This doesn't work in this chapter because we need to modify the array in place.
"""

#solution 3 two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L
"""
Time complexity: O(n)
Space complexity: O(1)
Explanation: 
we start at second value. why? because first value is always unique.
we use two pointers L (left) and R (right).

L points to the index where the next unique element should be placed

 R points to the index of the current value (the looping pointer)

both pointers start at 1 (second element) because first element is always unique.
we compare R with R - 1

if equal. that means we have a duplicate. we don't copy anything yet.
but we now know that this is where we will put the next unique value (the next unique value R will be pointing at).
then we increment R to check the next value. while L is still at the last unique value.

if not equal this means we have a unique value (right must be higher because the array is sorted)
we copy the value at R (new unique value) with the value at L (last unique value). then we increment L and R.

repeat the above

example: (3,3,3,5,…) L starts at the second 3. When R reaches 5, we copy 5 into index L and move L forward.
The third 3 is not changed unless R later finds another new unique value to copy.

note: R is auto incremented by the for loop.
the array could be empty so it's best if check if the array is empty first.

how many unique elements are there? the answer is L.
why? because we started at 1 and incremented L every time we found a new unique value.

"""