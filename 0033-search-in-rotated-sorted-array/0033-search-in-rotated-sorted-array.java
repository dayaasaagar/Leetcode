class Solution {
    public int search(int[] nums, int target) {
        
        int low =0;
        int high = nums.length-1;

        while(low<=high)
        {
          int mid = (low+high) /2;

          if(nums[mid]==target)
          {
            return mid;
          }

          //first we have to determine which side is sorted.

          if(nums[mid]>=nums[low])
          {
            //left side is sorted
            //now we have to determine which side does the target lies 
            if(target>=nums[low] && target<=nums[mid])
            {
                //search in left half
                high = mid-1;
            }
            else
            {
                low = mid+1;
            }
          }
          else
          {
            if(target<=nums[high] && target>=nums[mid])
            {
                //search in right half
                low = mid +1;
            }
            else
            {   //search in left half
                high = mid -1;
            }
          }
        }
        return -1;
    }
}