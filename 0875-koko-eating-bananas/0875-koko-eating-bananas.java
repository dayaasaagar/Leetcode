class Solution {
    public int minEatingSpeed(int[] piles, int h) {
  

        Arrays.sort(piles);
        int low = 1;
        int high= Arrays.stream(piles).max().getAsInt();

        while(low<high)
        {
            int mid= (low+high)/2;
            int total =0;
            for(int pile:piles)
            {
                total+=Math.ceil((double) pile/mid);
            }
            if(total<=h)
            {
                high = mid;
            }
            else 
            {
                low = mid+1;
            }
        }
        return low;
        
    }
}