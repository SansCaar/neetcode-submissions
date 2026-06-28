class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
       const res = {};
        for(let str of strs){
            let count = Array(26).fill(0);
            for(let s of str){
                let idx = s.charCodeAt(0) -'a'.charCodeAt(0)
                count[idx] += 1;
            }
            let key = count.join(',');
            if(!res[key]) res[key] = [];
            res[key].push(str);
        }
        return Object.values(res)
    }
}
