class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        arr=[]
        ls=0
     
    
        for i in range(n):
            arr.append(start+2*i)

        for i in arr:
            ls^=i

        
        return ls

        
        
        