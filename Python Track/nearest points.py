class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        dist = inf
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                smalldis = abs(points[i][0] - x) +abs(points[i][1] - y)
                if smalldis < dist:
                    dist = smalldis
                    index = i
        return index
               
