class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        visited = set()
        visited.add(0)
        while queue:
            room = queue.popleft()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
        if len(visited) == len(rooms):
            return True
        
