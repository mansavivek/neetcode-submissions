class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(int(2*stack[-1]))
            elif i == "+":
                stack.append(int(stack[-1]+stack[-2]))
            else:
                stack.append(int(i))
        return sum(stack)
            
        