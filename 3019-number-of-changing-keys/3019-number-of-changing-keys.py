class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        prev = s[0].lower()

        for i in range(1,len(s)):
            if s[i].lower()!=prev:
                count+=1
            prev = s[i].lower()

        return count

        