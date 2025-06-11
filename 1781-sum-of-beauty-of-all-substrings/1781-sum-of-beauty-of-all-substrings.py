class Solution:
    def beautySum(self, s: str) -> int:
        total=0

        for i in range(len(s)):
            freq =[0]*26
            for j in range(i,len(s)):
                idx = ord(s[j]) - ord('a')
                freq[idx]+=1
                max_f = max(freq)
                min_f = min(f for f in freq if f>0)
                total+= max_f-min_f
        return total


        