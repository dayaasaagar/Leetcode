class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for i in s:
            
            if i in ['(','{','[']:
                st.append(i)
            elif(i==')' and not len(st)==0 and st[-1]=='('):
                st.pop()
            elif(i=='}' and not len(st)==0 and st[-1]=='{'):
                st.pop()
            elif(i==']' and not len(st)==0 and st[-1]=='['):
                st.pop()
            else:
                return False
        return st==[]  
