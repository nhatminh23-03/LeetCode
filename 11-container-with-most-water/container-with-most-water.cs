public class Solution {
    public int MaxArea(int[] height) {
        int left = 0;
        int right = height.Length - 1;
        int max_area = 0;
        while (left < right){
            int area = (right - left) * Math.Min(height[right], height[left]);
            max_area = Math.Max(area, max_area);
            if (height[right] > height[left]){
                left++;
            } else {
                right--;
            }
        }
        return max_area;
        
    }
}