class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int i=0;
        int j=numbers.length-1;
        int[] result = new int[3];

        while(i<j)
        {
            int sum = numbers[i]+numbers[j];
            if(sum<target)
            {
                i++;
            }
            else if(sum>target)
            {
                j--;
            }
            if(sum==target)
            {
             return new int[]{i+1,j+1}; 
            }


        }
        return new int[]{};
    }
}