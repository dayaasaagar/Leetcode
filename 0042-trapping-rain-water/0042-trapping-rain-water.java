class Solution {
    public int trap(int[] height) {

        //logic: take min of the max left and max right 
        //o(n) solution
        // alternative: left max array, right max array and array for computing the min of each left max and right max. space complexity increases to big o n.




        //using two pointer technique


        int leftMax=0;
        int rightMax=0;
        int left=0;
        int right = height.length-1;
        int res=0;


        while(left<right)
        {
            if(height[left]<height[right])
            {
                if(height[left]>=leftMax)
                {
                    leftMax=height[left];
                }
                else
                {
                    res+=leftMax-height[left];
                }
                left++;
            }
            else
            {
                if(height[right]>=rightMax)
                {
                    rightMax=height[right];
                }
                else
                {
                    res+=rightMax-height[right];
                }
                right--;
            }

        }

        return res;
    }
}