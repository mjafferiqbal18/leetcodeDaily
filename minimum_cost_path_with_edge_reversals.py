class Solution:
    """
    Problem: 3650. Minimum Cost Path with Edge Reversals
    https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

    Intuition:
    - The question says that once you're at node u, you can either pick:
        - you regular outgoing edges OR
        - any incoming edge, reversed with weight*2
        - you wouldnt go u->v->u because cost(u->v->u) would be more than staying at u, since weights are positive
    - Then you can just add reverse edges (with double weight) in the adjacency dict
    - Run dijstra

    Time:
    - O(V+2E log V)

    Space:
    - O(V+E)
    """

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj={}
        for u,v,w in edges:
            if u not in adj:
                adj[u]=set()
            adj[u].add((v,w)) #src -> dst,weight
            if v not in adj:
                adj[v]=set()
            adj[v].add((u,w*2)) #dst -> src, weight*2
        
        return self.dijkstra(adj,n)



    def dijkstra(self,adj,n):
        distances = [float('inf')]*n
        distances[0] = 0
        minHeap = [(0,0)] #dist from src, node
        heapq.heapify(minHeap)
        visited = set()

        while minHeap:
            distFromSrc, node = heapq.heappop(minHeap)
            visited.add(node)

            if distFromSrc < distances[node]:
                distances[node] = distFromSrc

            if node in adj:
                for dst, w in adj[node]:
                    if dst not in visited and distances[node]+w < distances[dst]:
                        heapq.heappush(minHeap, (distances[node]+w,dst))
        
        return distances[n-1] if distances[n-1]!=float('inf') else -1

        