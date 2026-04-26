class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []

        for i in range(len(position)):
            car = [position[i], speed[i]]
            cars.append(car)
        
        cars.sort(reverse=True)

        stack.append((target - cars[0][0]) / cars[0][1])
        for car in cars:
            time = (target - car[0]) / car[1]
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)