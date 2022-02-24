from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # if length is 0 then return
        if length == 0: return []

        # cache array to return the answer
        cache = [None] * length
        # stores the previous value as loop goes from 0 to n index (forward_previous)
        f_prev = 1
        # stores the previous value as loop goes from n to 0 index (backward_previous
        b_prev = 1
        # products are required to store the previous products to be used in the next loop
        # store the product of all the nums before the current value in loop 0 to n (forward product)
        f_prod = 1
        # store the product of all the nums before the current value in loop n to 0 (backword product)
        b_prod = 1

        for i in range(length):
            
            # updates the product by multiplying with the new previous value
            f_prod = f_prod * f_prev
            # if the current index has no value assign 1 because anything multiplied by 1 is that number
            # it safe to use 1 and thus we can initialise the cache for that index
            if cache[i] == None: 
                cache[i] = 1
            # update the cache, especially important when the looping backwords reaches the first indexes to update these indexes
            cache[i] = cache[i] * f_prod
            # store the previous value to update the front_previous
            f_prev = nums[i]

            # same logic
            b_prod = b_prod * b_prev
            if not cache[length - (i + 1)]: 
                cache[length - (i + 1)] = 1
            # update the cache, especially important when the looping forwards reaches the last indexes to update these indexes
            cache[length - (i + 1)] =  cache[length - (i + 1)] * b_prod
            b_prev = nums[length - (i + 1)]

            print(f_prod, cache, f_prev, b_prod, cache, b_prev)

        return cache
           

ans = Solution()
print(ans.productExceptSelf([10, 3, 5, 6, 2])) 


# Trapping rain water 
# paint house ii
# minimum diff in sums after removal of elements
# maximum product subarray // imp