class Solution {
    public String removeKdigits(String num, int k) {

        Stack<Character> st = new Stack<>();

        for(char ch:num.toCharArray())
        {
            while(!st.isEmpty() && k>0 && st.peek()>ch)
            {
                st.pop();
                k--;
            }
            st.push(ch);
        }

        while(k>0)
        {
            st.pop();
            k--;
        }

        StringBuilder ns = new StringBuilder();
        for(char c:st)
        {
            ns.append(c);
        }

        while(ns.length()>0 && ns.charAt(0)=='0')
        {
            ns.deleteCharAt(0);
        }
        return ns.length()==0 ? "0": ns.toString();

        
    }
}