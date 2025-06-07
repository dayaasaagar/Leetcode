class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        countdict= Counter(words)
        wordlist = sorted(countdict.items(),key=lambda x:(-x[1],x[0]))
        return [word for word,count in wordlist[:k]]