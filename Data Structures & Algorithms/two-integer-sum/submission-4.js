class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
       let map = new Object()
       for(let i=0; i<nums.length;i++){
        map[target - nums[i]] = i
       }
       for(let i=0; i<nums.length;i++){
        if(map.hasOwnProperty(nums[i])){
            let mapIndexValue = map[nums[i]]
            if(i !== mapIndexValue) return [i, mapIndexValue]
        }
       }
    }
}
