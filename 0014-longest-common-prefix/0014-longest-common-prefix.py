class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first_word = strs[0]
        if not strs:
            return ""
        prefix=""
        for i in range(len(first_word)):
            char = first_word[i]

            for word in strs[1:]:

                if i>=len(word) or word[i]!=char:
                    return prefix

            prefix+=char
        return prefix

        

        