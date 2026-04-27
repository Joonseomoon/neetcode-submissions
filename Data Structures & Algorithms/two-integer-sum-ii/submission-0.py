class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index2 = 1
        for index1 in enumerate(numbers):
            diff = target - numbers[index1]
            while numbers[index2] <= diff:
                if diff == numbers[index2]:
                    return [index1 + 1, index2 + 1]
                index2 += 1
