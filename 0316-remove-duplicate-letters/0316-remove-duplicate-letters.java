class Solution {
    public String removeDuplicateLetters(String s) {
        Stack<Character> st = new Stack<>();
        int[] last = new int[26];
        boolean[] seen = new boolean[26];

        // store last occurrence of each character
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }

        for (int j = 0; j < s.length(); j++) {
            char ch = s.charAt(j);

            if (seen[ch - 'a']) continue;

            while (!st.isEmpty() &&
                   st.peek() > ch &&
                   last[st.peek() - 'a'] > j) {
                seen[st.peek() - 'a'] = false;
                st.pop();
            }

            st.push(ch);
            seen[ch - 'a'] = true;
        }

        StringBuilder result = new StringBuilder();
        for (char c : st) {
            result.append(c);
        }

        return result.toString();
    }
}