public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        List<IList<int>> res = new List<IList<int>>();
        
        for (int i = 0; i < nums.Length; i++){
            if (i > 0 && nums[i] == nums[i - 1]){
                continue;
            }

            int left = i + 1;
            int right = nums.Length - 1;
            while (left < right){
                int total = nums[i] + nums[left] + nums[right];
                if (total > 0){
                    right--;
                } else if (total < 0){
                    left++;
                } else {
                    res.Add(new List<int> {nums[i], nums[left], nums[right]});
                    left++;
                    while (left < right && nums[left] == nums[left - 1]){
                        left++;
                    }
                }
            }
        }
        return res;
    }
}