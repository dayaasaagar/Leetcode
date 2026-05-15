class Solution {
    public int[][] kClosest(int[][] points, int k) {
        


        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b)->b[0]-a[0]);

        for(int[] point:points)
        {
           int x = point[0];
           int y = point[1];

           int dist = x*x+y*y;
           maxHeap.add(new int[]{dist,x,y});
           if(maxHeap.size()>k)
           { maxHeap.poll();
           }

          
        }
        int[][] result = new int[k][2];
        int i=0;
        while(!maxHeap.isEmpty())
        {
          int[] point = maxHeap.poll();
          result[i++]=new int[] {point[1],point[2]};
        }

        return result;
    }
}