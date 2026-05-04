class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {

        Deque<Integer> queue = new LinkedList<>();

        int[] result = new int[nums.length - k + 1];
        int idx=0;

        for(int i=0;i<nums.length;i++)
        {   //remove elements from the window
            while(!queue.isEmpty() && queue.peekFirst()<i-k+1)
            {
                queue.pollFirst();
            }
            while(!queue.isEmpty() && nums[queue.peekLast()]<nums[i])
            {
                queue.pollLast();
            }
            queue.offerLast(i);

            if(i>=k-1)
            {
                result[idx++]= nums[queue.peekFirst()];
            }
        }
        return result;
        
    }
}