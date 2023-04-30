class Solution:
    def maxProduct(self, words: List[str]) -> int:
        w = [0] * len(words)
        ans = 0

        for i, word in enumerate(words):
            for letter in word:
                w[i] |= (1 << (ord(letter) - ord('a')))

        for i in range(len(w)):
            for j in range(len(w)):
                if w[i] & w[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
