class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(int(2*stack[-1]))
            elif i == "+":
                stack.append(int(stack[-1]+stack[-2]))
            else:
                stack.append(int(i))
        while stack:
            res += stack.pop()
        return res
            
        