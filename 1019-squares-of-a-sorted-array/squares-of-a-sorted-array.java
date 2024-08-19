class Solution {
    public int[] sortedSquares(int[] nums) {
        /*for (int i = 0; i < nums.length; i++){
           nums[i] = nums[i] * nums[i];
        }
        
        Arrays.sort(nums);
        
        return nums;*/
        
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        
        int[] result = new int[n];
        
        for (int i = n - 1; i >= 0 ; i--){
            if (Math.abs(nums[left]) > Math.abs(nums[right])){
                result[i] = nums[left] * nums[left];
                left++;
            } else {
                result[i] = nums[right] * nums[right];
                right--;
            }
        }
        return result;
        
    }
}