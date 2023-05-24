''''

'''

from typing import List

class Solution(object):
    def twoSum(self,nums,target):
        for index,value in enumerate(nums):
            for secondIndex in range(index+1,len(nums)):
                if value + nums[secondIndex] == target:
                    return[index,secondIndex]
                
nums=[3,2,4]
print(Solution().twoSum(nums,6))