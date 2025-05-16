class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]

        def dfs(start,path:List[str]):

            if start == len(s):
                res.append(path[:])
                return

            
            for end in range(start+1,len(s)+1):
                prefix = s[start:end]

                if prefix == prefix[::-1]:
                    path.append(prefix)
                    dfs(end,path)
                    path.pop()
            
        

        dfs(0,[])
        return res


                

