class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        st ={}
        ts={}


        for c,t in zip(s,t):

            if c in st and st[c]!=t:
                return False
            if t in ts and ts[t]!=c:
                return False
            
            st[c]=t
            ts[t]=c
        return True

