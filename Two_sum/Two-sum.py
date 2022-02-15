class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) == 0: 
            return False
        # hash map that stores the index of a parrticular number eg - obj[particular_num] = index
        obj = {}
        #  stores the indexes that sums up to form the target
        answer = []
        difference = 0
        for i in range(len(nums)): 
            # find the diff between target and the current number
            difference = target - nums[i]  
            # if the difference in the hash map then the answer is the hash map and the current index eg - [hash_map_index, current_index]
            # we got the answer, just return
            if difference in obj:
                    answer = [obj[difference], i]
                    return answer
            else: 
                # else store the current index using the current number as key
                # because the next correct difference will be this current number if any matches that is
                obj[nums[i]] = i
        # if here it means nothing summed up to target and just return false
        return False
        
ans = Solution()
print(ans.twoSum([2,4,5], 7))