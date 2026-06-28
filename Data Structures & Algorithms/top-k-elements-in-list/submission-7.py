# //map 
# //2 : 1
# //3 : 2

# [0, 0, [3, 3], 0, 0] len = n

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else: 
                counts[num] = 1
        sorted_list = [0] * (len(nums)+1)

        
        for idx, (key, val) in enumerate(counts.items()):
            if not sorted_list[val]:
                sorted_list[val] = []
            sorted_list[val].append(key)
        
        print(sorted_list)
        
        res = []
        count = 0
        for i in range(len(sorted_list) -1, -1, -1):
            if sorted_list[i]:
                for num in sorted_list[i]:
                    if count == k:
                        break
                    res.append(num)
                    count += 1
                    
                    

        return res

