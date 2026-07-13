class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { c : [] for c in range(numCourses)}
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        res = []

        def dfs(crs):
            res.append(crs)
            indegree[crs] -= 1 # marking already processed for outer loop below
            for nxt in adj[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    dfs(nxt)

        for c in range(numCourses):
            if indegree[c] == 0:
                dfs(c)

        return res if len(res) == numCourses else []