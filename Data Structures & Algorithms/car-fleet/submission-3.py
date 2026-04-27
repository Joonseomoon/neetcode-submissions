class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        prevTime = (target - cars[0][0]) / cars[0][1]
        for p, s in cars:
            currtime = (target - p) / s
            if currtime > prevTime:
                fleets += 1
                prevTime = currTime
        return len(stack)