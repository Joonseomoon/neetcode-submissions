class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)

        def transform(word, nei):
            count = 0
            for i in range(len(word)):
                if word[i] != nei[i]:
                    count += 1 
            if count == 1:
                return True
            return False

        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for word in wordList:
                    if word not in visited:
                        if transform(cur, word):
                            q.append(word)
                            visited.add(word)
            res += 1
        return 0
                    