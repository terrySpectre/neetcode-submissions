class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        pair.sort(reverse=True)
        car_fleet = 0
        for i in pair:
            if stack and ((target - i[0]) / i[1]) > stack[-1]:
                car_fleet += 1   
                stack.append((target - i[0]) / i[1]) 
            elif not stack:
                stack.append((target - i[0]) / i[1])     
                car_fleet += 1
            else:
                stack.append(stack[-1])     
        return car_fleet
        

        