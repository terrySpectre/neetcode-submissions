class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = []
        stack = []
        for p, s in zip(position, speed):
            pos_and_speed.append((p, s))
        pos_and_speed.sort(reverse=True)
        for i in pos_and_speed:
            if stack and ((target - i[0]) / i[1]) < stack[-1]:
                stack.append(stack[-1])
            else:
                stack.append((target - i[0]) / i[1])
        car_fleet = 1
        for j in range(1, len(stack)):
            if stack[j] > stack[j-1]:
                car_fleet += 1
        return car_fleet
        

        