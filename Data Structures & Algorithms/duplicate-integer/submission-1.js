class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let n = new Set();
        for(const num of nums){
            if(n.has(num)){
                return true;
            }
            n.add(num);
        }
        return false
    }
}
