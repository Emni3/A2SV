class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = 0
        basket = defaultdict(int)
        left = 0
        for right in range(len(fruits)):
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            basket[fruits[right]] += 1
            if len(basket)<=2:
                picked = max(right - left + 1, picked)
           
            
        return picked
            
            