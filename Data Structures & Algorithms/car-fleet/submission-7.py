class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = []
        stack = []
        for p, s in zip(position, speed):
            pos_and_speed.append((p, s))
        pos_and_speed.sort(reverse=True)
        for i in pos_and_speed:
            if stack and ((target - i[0]) / i[1]) <= stack[-1]:
                continue
            else:
                stack.append((target - i[0]) / i[1])
        return len(stack)
        


        