class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for ( int i = 0; i < nums.length; i++){
            int reqNum = target - nums[i];
            if (numMap.containsKey(reqNum)){
                return new int[]{i, numMap.get(reqNum)};
            }
            numMap.put(nums[i], i);
        }
        return new int[]{};
        
        
    }
}