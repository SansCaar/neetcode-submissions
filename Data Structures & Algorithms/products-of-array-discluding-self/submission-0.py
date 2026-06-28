class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        prefix , postfix = 1, 1
        output=[1] * (len(nums))

        for i in range(0, len(nums)):
            # Multiply the accumulated product before the index
            output[i] *= prefix
            # Accumulate the multiplication in prefix up to the current index
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            #Multiply the accumulated product after the index
            output[i] *= postfix
            # Accumulate the product in postfix behind the current index
            postfix *= nums[i]
        return output
