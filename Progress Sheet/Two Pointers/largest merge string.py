class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        merged = ''
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1) and ptr2 < len(word2):
                if word1[ptr1:] >= word2[ptr2:]:
                    merged  += word1[ptr1]
                    ptr1 += 1
                elif word2[ptr2:] >= word1[ptr1:]:
                    merged += word2[ptr2]
                    ptr2 += 1
            elif ptr1 < len(word1):
                merged += word1[ptr1]
                ptr1 += 1
            elif ptr2 < len(word2):
                merged += word2[ptr2]
                ptr2 += 1
        return merged
