class Solution {
    public int characterReplacement(String s, int k) {
        int[] counter = new int[26];
        int i=0;
        int max_freq=0;
        int max_count=0;
        for(int j=0;j<s.length();j++)
        {  char ch = s.charAt(j);
            counter[ch-'A']++;
            max_count = Math.max(max_count,counter[ch-'A']);
            while(((j-i+1)-max_count)>k)
            {
                counter[s.charAt(i)-'A']--;
                i++;
            }
            max_freq=Math.max(max_freq,(j-i+1));
        }
        return max_freq;
    }
}