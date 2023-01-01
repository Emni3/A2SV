class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(min(len(word1), len(word2))):
            merged += word1[i]
            merged += word2[i]
        if len(word1)<len(word2):
            merged += word2[len(word1):]
        else:
            merged += word1[len(word2):]
        
        return merged
