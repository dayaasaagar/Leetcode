class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set= set()

        i=0
        max_length =0
        for j in range(len(s)):

            while s[j] in new_set:
                new_set.remove(s[i])
                i+=1
            
            new_set.add(s[j])
            max_length = max(max_length,j-i+1)

        return max_length
