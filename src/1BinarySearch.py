''''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)-1

        while(begin <= end):
            half = int((begin + end)/2)

            if nums[half] == target:
                return half

            if nums[half] < target:
                begin += 1             
            else:
                if(end == half):
                    break
                end = half
        return -1



nums = [-1,0,3,5,9,12]
print(Solution().search(nums,target=2) == -1)           
print(Solution().search(nums,target=9) == 4)

nums = [-1,0,3,5,9,12]
print(Solution().search(nums,target=8) == -1)           
print(Solution().search(nums,target=3) == 2)

nums = [-2,-1,0,2,3,4,5,9,12,13]
print(Solution().search(nums,target=-3) == -1)           
print(Solution().search(nums,target=5) == 6)

nums = [-2,-1,0,2,3,4,5,9,12,13]
print(Solution().search(nums,target=-14) == -1)           
print(Solution().search(nums,target=-2) == 0)
print(Solution().search(nums,target=13) == 9)           
print(Solution().search(nums,target=-1) == 1)
print(Solution().search(nums,target=12) == 8)