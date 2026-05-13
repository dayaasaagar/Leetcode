class Solution {
    public int findMin(int[] nums) {
        // In a rotated sorted array we have left sorted position and a right sorted position 
        // we use binary search
        // if the middle element is smaller than the left most element it means it is going to be smaller than the rest of the rest of elements in the subarray. Then we return the minimum.
        // if the middle element is bigger than the left most element it means we have to search it in the right part of the sorted array, where smaller elements may be present
        // if the middle element is not bigger than the left most element, we have to search it in the right part of the sorted array.
        //edge case: if the middle element is smaller than the left most element it means we have found the minimum and we will return the element. 


        int low =0;
        int high = nums.length-1;
        int ans=0;

        while(low<high)
        {
            int mid = (low+high)/2;

            if(nums[mid]>nums[high])
            {
                //this means mid is in the left sorted portion
                //minimum will be in the right sorted portion
                low = mid+1;
            }
            else
            {
                //this means mid is in the right sorted portion
                //minimum will be the right 
                high = mid;

            }


        }
        return nums[low];
        
    }
}