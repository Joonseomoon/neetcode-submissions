class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses 
        adj = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = collections.deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        finish, res = 0, []

        while q:
            crs = q.popleft()
            res.append(crs)
            finish += 1

            for c in adj[crs]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            
        if finish != numCourses:
            return []
        return res