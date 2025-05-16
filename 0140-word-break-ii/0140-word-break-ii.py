class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set=set(wordDict)
        memo = {}

        def dfs(start):

            if start in memo:
                return memo[start]
            elif start == len(s):
                return [""]
            
            res =[]
            for end in range(start+1,len(s)+1):
                word = s[start:end]
                if word in word_set:
                    rest_sentence = dfs(end)

                    for sentence in rest_sentence:
                        if sentence:
                            res.append(word+" "+sentence)
                        else:
                            res.append(word)

            memo[start]=res
            return res
        return dfs(0)