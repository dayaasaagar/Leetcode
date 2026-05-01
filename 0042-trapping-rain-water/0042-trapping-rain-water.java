class Solution {
    public int trap(int[] height) {

        //logic: take min of the max left and max right 
        //o(n) solution
        // alternative: left max array, right max array and array for computing the min of each left max and right max. space complexity increases to big o n.




        //using two pointer technique


        // int leftMax=0;
        // int rightMax=0;
        // int left=0;
        // int right = height.length-1;
        // int res=0;


        // while(left<right)
        // {
        //     if(height[left]<height[right])
        //     {
        //         if(height[left]>=leftMax)
        //         {
        //             leftMax=height[left];
        //         }
        //         else
        //         {
        //             res+=leftMax-height[left];
        //         }
        //         left++;
        //     }
        //     else
        //     {
        //         if(height[right]>=rightMax)
        //         {
        //             rightMax=height[right];
        //         }
        //         else
        //         {
        //             res+=rightMax-height[right];
        //         }
        //         right--;
        //     }

        // }

        // return res;



        int[] leftMax = new int[height.length];
        int[] rightMax = new int[height.length];
        int ans=0;
    

        leftMax[0]=height[0]; //maximum of left of the oth element will be 0th element
        for(int i=1;i<height.length;i++)
        {
            leftMax[i]=Math.max(leftMax[i-1],height[i]);
        }
        rightMax[height.length-1]=height[height.length-1];
        for(int k=height.length-2;k>=0;k--)
        {
            rightMax[k]=Math.max(rightMax[k+1],height[k]);
        }
        for(int j=0;j<height.length;j++)
        {
           ans+= Math.min(leftMax[j],rightMax[j])-height[j];

        }

        return ans;

    }
}