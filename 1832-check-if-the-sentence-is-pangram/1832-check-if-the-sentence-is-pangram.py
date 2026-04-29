class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count_new = Counter(sentence)
        if len(count_new)==26:
            return True
        else:
            return False        