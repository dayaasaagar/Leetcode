class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {


        //use a counter as a key
        //use a hashmap 


        HashMap<String,List<String>> map = new HashMap<>();
       for(String word:strs)
       {
         //step1: create a counter array
        int[] counter = new int[26];
        for(char ch:word.toCharArray())
        {
            counter[ch-'a']++;
        }

        //convert this into string builder because we cannot use array to compare 

        StringBuilder st = new StringBuilder();
        for(int num:counter)
        {
            st.append(num).append('#');
        }

        String key = st.toString();

        map.computeIfAbsent(key,k->new ArrayList<>()).add(word);

       }
       return new ArrayList<>(map.values());
        
        
    }
}