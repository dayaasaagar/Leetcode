class Solution {
    public String expand(String s,int i,int j)
    {
        while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j))
        {
            i-=1;
            j+=1;
        }
        return s.substring(i+1,j);
    }
    public String longestPalindrome(String s) {

        if (s== null|| s.length()<1) return "";

        String longest ="";

        for(int i=0;i<s.length();i++)
        {
            String odd = expand(s,i,i);
            String even= expand(s,i,i+1);
            if(odd.length()>longest.length())
            {
                longest=odd;
            }
            if(even.length()>longest.length())
            {
                    longest=even;
            }
        }
        return longest;
    
    }
}