class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxcount =0;
       
        for(int i=0;i<sentences.length;i++)
        {   int count =1;
            for(char ch:sentences[i].toCharArray())
            {
                if(ch==' ')
                {
                        count++;

                }
                maxcount = Math.max(maxcount,count);
            }
        }
        return maxcount;
        
    }
}