class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        possible = True
        maxi = 0
        prev = 0
        for trip in trips:
            maxi = max(trip[-1], maxi)

        travel = [0 for _ in range(maxi + 1)]
        for trip in trips:
            travel[trip[1]] += trip[0]
            travel[trip[2]] -= trip[0]

        for i in range(len(travel)):
            travel[i] += prev
            prev = travel[i]
        
        for i in travel:
            if i > capacity:
                return not possible 
                
        return possible
