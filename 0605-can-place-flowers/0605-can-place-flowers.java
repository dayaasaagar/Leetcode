class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int ne= flowerbed.length;
        int interval =0;
        for(int i=0;i<flowerbed.length;i++)
        {
            if(flowerbed[i]==0)
            {
                if((i==0||flowerbed[i-1]==0)&&(i==ne-1||flowerbed[i+1]==0))
                {
                    flowerbed[i]=1;
                    interval++;
                }
            }
            if(interval==n)
            {
                return true;
            }
        }
        return interval>=n;

    }
}