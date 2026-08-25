class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final = [float('-inf'), float('-inf'), float('-inf')]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                final = [max(final[0], a),
                         max(final[1], b),
                         max(final[2], c)]
            if final == target:
                return True
        return False
