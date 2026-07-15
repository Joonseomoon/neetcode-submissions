class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {n : [] for n in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return 
            visited.add(node)
            for nei in adj[node]:
                if nei != prev:
                    dfs(nei, node)
        
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res += 1
        
        return res
