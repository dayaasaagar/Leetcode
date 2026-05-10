class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        // Sort indices by position descending
        Arrays.sort(idx, (a, b) -> position[b] - position[a]);

        int fleets = 0;
        double maxTime = 0;

        for (int i : idx) {
            double time = (double)(target - position[i]) / speed[i];
            if (time > maxTime) {   // new fleet
                maxTime = time;
                fleets++;
            }
            // else: merges with fleet ahead, skip
        }

        return fleets;
    }
}