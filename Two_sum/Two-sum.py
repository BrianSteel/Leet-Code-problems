class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) == 0: 
            return False
    
        obj = {}
        answer = []
        difference = 0
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in obj and obj[difference][0] == 1:
                    answer = [obj[difference][1], i]
                    return answer
            else: 
                obj[nums[i]] = [1, i] 
        return False
        