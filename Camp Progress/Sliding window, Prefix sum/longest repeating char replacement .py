class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        total = 0
        sub = defaultdict(int)
        for right in range(len(s)):
            sub[s[right]] += 1
            total += 1
            maxi = max(sub.values())
            while total - maxi > k:
                sub[s[left]] -= 1
                max_len = max(total-1, max_len)
                total -= 1
                maxi = max(sub.values())
                left += 1
        max_len = max(total, max_len)
        return max_len
