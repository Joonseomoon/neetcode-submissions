class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for n in range(n)]
        for src, trg in edges:
            adj[src].append(trg)
            adj[trg].append(src)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n

