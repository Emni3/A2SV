
class Solution:
    def insert(self, group, ans):
        for x in str(group):
            ans.append(x)
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 1
        group = 1
        length = 0
        ans = []
        if len(chars) == 1:
            print(chars)
            return 1
        while right < len(chars):
            if chars[right] == chars[left]:
                group += 1
                right += 1

            else:
                ans.append(chars[left])
                print(chars[left], group)
                if group > 1:
                    self.insert(group, ans)
                group = 0
                left = right
        #print((str(group).split()))
        if group > 1:
            ans.append(chars[-1])
            self.insert(group, ans)
        chars[:] = ans
        #print(chars) 
        return len(chars)
