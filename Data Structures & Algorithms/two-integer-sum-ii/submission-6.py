class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index2 = 1
        for index1 in range(len(numbers) - 1):
            index2 = index1 + 1
            diff = target - numbers[index1]
            while index2 <= len(numbers) - 1:
                if diff == numbers[index2]:
                    return [index1 + 1, index2 + 1]
                index2 += 1
        return []