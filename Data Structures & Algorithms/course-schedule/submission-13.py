class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses # number of prerequisites node has
        adj = [[] for _ in range(numCourses)] # the classes that node is a prerequisite for
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            for i in range(len(q)):
                a = q.popleft()
                for b in adj[a]:
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        q.append(b)
                finished += 1
        return finished == numCourses
        