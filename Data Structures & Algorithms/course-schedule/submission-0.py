class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        #adjacency matrix completed
        indegree = [0] * numCourses
        for e in graph:
            for neighbor in e:
                indegree[neighbor]+=1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        s = set()
        while(queue):
            node = queue.pop() #stack implementation
            s.add(node)
            for neighbor in graph[node]:
                indegree[neighbor] -=1 
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(s) == numCourses:
            return True
        return False
