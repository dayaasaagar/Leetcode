class Solution {
    public int maxProduct(int[] nums) {
        int max_sum = nums[0];
        int min_sum = nums[0];
        int result  = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int temp = max_sum; // save before overwriting
            max_sum = Math.max(nums[i], Math.max(nums[i] * max_sum, nums[i] * min_sum));
            min_sum = Math.min(nums[i], Math.min(nums[i] * temp,    nums[i] * min_sum));
            result  = Math.max(result, max_sum);
        }
        return result;
    }
}