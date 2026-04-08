class Solution {
    public int maxSubArray(int[] nums) {

        int current_sum =nums[0];
        int max_sum =nums[0];

        for(int i=1;i<=nums.length-1;i++)
        {
            current_sum=Math.max(nums[i],nums[i]+current_sum); //decision to select a current number or not 1. we will selection only when if the current sum is greater than the previous one. 
            max_sum=Math.max(max_sum,current_sum);
        }

      return max_sum;


    }
}