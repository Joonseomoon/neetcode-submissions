class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = collections.defaultdict(List)
        for a, b in prerequisites:
            if a in hashmap:
                hashmap[a].append(b)
            else:
                hashmap[a] = [b]
        
        def dfs(c, visited):
            if c not in hashmap:
                return True
            visited.add(c)
            for b in hashmap[c]:
                if b in visited:
                    return False
                if not dfs(b, visited):
                    return False
            visited.remove(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True