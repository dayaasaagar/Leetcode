class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        new_array = sorted(zip(position,speed),reverse= True)
        stack = []
        for pos,spd in new_array:
            time =(target-pos) / spd 
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)