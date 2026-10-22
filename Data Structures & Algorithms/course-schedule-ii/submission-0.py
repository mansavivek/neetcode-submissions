class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for s,e in prerequisites:
            adj[s].append(e)
            indegree[e]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            course = q.popleft()
            finish +=1
            res.append(course)
            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt]== 0:
                    q.append(nxt)
        return res[::-1] if finish == numCourses else []
        