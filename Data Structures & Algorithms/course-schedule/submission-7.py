class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = collections.defaultdict(List)
        for a, b in prerequisites:
            if a in hashmap:
                hashmap[a].append(b)
            else:
                hashmap[a] = [b]

        visited = set()
        
        def dfs(c):
            if c in visited:
                return False
            if c not in hashmap:
                return True
            visited.add(c)
            for b in hashmap[c]:
                if not dfs(b):
                    return False
            visited.remove(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True