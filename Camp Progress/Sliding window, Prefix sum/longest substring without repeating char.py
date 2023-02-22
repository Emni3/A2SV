class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        sub = {}
        right,left = 0 ,0

        for right, char in enumerate(s):
            sub[char] = sub.get(char, 0)  +  1

            while left < right and  sub[char] > 1:
                sub[s[left]] -= 1

                if sub[s[left]] == 0:
                    sub.pop(s[left])
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

