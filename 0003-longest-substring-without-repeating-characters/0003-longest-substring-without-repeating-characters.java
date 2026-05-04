class Solution {
    public int lengthOfLongestSubstring(String s) {
        //use a hashset
        // use sldiing window
        // shrink the window if the character is already in the hashset


        int i=0;
        int max_len=0;
        HashSet<Character> set = new HashSet();
        for(int j=0;j<s.length();j++)
        {   char ch = s.charAt(j);
            while(set.contains(ch))
            {
                set.remove(s.charAt(i)); //shrink the window
                i++;
            }
            set.add(ch);
            max_len=Math.max(j-i+1,max_len);
        }
        return max_len;
        
    }
}