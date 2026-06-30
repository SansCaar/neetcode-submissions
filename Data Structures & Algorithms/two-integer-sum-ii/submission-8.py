class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # We use a two pointers to track our largest number and smallest
        l , r = 0, len(numbers) -1
        while l < r:
            s = numbers[l] + numbers[r]

            #if our sum is greater than the target we know that
            # the value needs to decrease so we move the right pointer and viceversa
            if s > target:
                r-=1
            elif s < target:
                l+=1
            elif s == target:
                return [l+1, r+1]
            
        
        return 
        