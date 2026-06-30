import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        possibleStarts = []
        numbers = set(nums)
        for n in nums:
            if n-1 not in numbers:
                possibleStarts.append(n)
        
        sequences = collections.defaultdict(list)
        for i in range(0, len(possibleStarts)):
            l = possibleStarts[i]
            while l in numbers:
                sequences[i].append(l)
                l+=1
        
        maxLength = 0

        for i in range(len(sequences)):
            if len(sequences[i]) > maxLength:
                maxLength = len(sequences[i])
        
        return maxLength


