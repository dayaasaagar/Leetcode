class Solution:
    def isValid(self, s: str) -> bool:



        st = deque()

        for i in s:

            if i == '(' or i=='[' or i=='{':
                st.append(i)
            elif (i == ')' and not len(st)==0 and st[-1]=='('):
                st.pop()
            elif (i == ']' and not len(st)==0 and st[-1]=='['):
                st.pop()
            elif (i == '}' and not len(st)==0 and st[-1]=='{'):
                st.pop()
            else:
                return False
        
        return True if len(st)==0 else False





            
