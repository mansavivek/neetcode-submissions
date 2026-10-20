from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        # visited = []
        for s,d,p in flights:
            adj[s].append([d,p])
        q = deque([(0,src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue
            
            for nextNode, weight in adj[node]:
                nextCost = cst + weight
                if nextCost < prices[nextNode]:
                    prices[nextNode] = nextCost
                    q.append((nextCost, nextNode, stops+1))
        
        return prices[dst] if prices[dst]!= float("inf") else-1

