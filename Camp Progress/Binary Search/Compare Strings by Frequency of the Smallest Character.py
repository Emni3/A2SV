class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        query = []
        word = []


        for i in queries:
            query.append(i.count(min(i)))
        for i in words:
            word.append(i.count(min(i)))
        word.sort()

        for q in query:
            num = len(words) - bisect.bisect_right(word, q)
            ans.append(num)

        return ans
