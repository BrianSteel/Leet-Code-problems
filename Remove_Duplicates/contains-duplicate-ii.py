from typing import List


class Solution:
    def containsNearbyDuplicate(self, List:List[int], k:int):
        length = len(List) # dont do len(List) - 1, range will take care of it

        hashMap = {}
        for index in range(length): # range will use length to create number 0 to length -1 
            key = List[index]
            if key in hashMap:
                hashMap[key].append(index)
                hash_map_length = len(hashMap[key])
                hash_last_value = hashMap[key][hash_map_length - 1]
                hash_second_last_value = hashMap[key][hash_map_length - 2]
                if (hash_last_value - hash_second_last_value) <= k: 
                    return True
            else:
                hashMap[key] = [index]

        return False
    def containsNearbyDuplicate(self, List:List[int], k:int):
        length = len(List) # dont do len(List) - 1, range will take care of it
 
        hashMap = {}
        for index in range(length): # range will use length to create number 0 to length -1 
            key = List[index]
            if key in hashMap and (index - hashMap[key]) <= k: 
                return True
            hashMap[key] = index

        return False
    
ans = Solution()
print(ans.containsNearbyDuplicate([3,3], 2))