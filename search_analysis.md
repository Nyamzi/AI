# Search Algorithms Analysis Report

**Student Name:** Wanyama David - 2022/BSE/016/PS
**Date:** 15th October,2025
**Assignment:** Project 0 - Uninformed Search Algorithms

---

## Section 1: Algorithm Analysis

### Theoretical Properties Comparison

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity | Data Structure |
|-----------|--------------|------------|-----------------|------------------|----------------|
| BFS       | ✓ Complete   | ✓ Optimal* | O(b^d)         | O(b^d)          | Queue (FIFO)   |
| DFS       | ✓ Finite**   | ✗ Not optimal | O(b^m)       | O(bm)           | Stack (LIFO)   |
| UCS       | ✓ Complete   | ✓ Optimal   | O(b^(C*/ε))    | O(b^(C*/ε))     | Priority Queue |

*BFS optimal for unweighted graphs  
**DFS complete only for finite search spaces

### When to Use Each Algorithm

TODO: Complete this section after implementing algorithms

**Breadth-First Search (BFS):**
- Best for: Unweighted shortest path problems, grid-based pathfinding, or when guaranteed optimality is required. It efficiently finds the shortest route in uniform-cost environments such as simple mazes or grids.

- Avoid when: Memory is limited or search depth is large, since BFS explores all nodes at a given level before going deeper, leading to exponential memory growth.

**Depth-First Search (DFS):**
- Best for: Exploring deep or infinite spaces where finding a solution quickly is more important than finding the shortest one. It’s also suitable for tree traversals, puzzles, and topological sorts.

- Avoid when: You need the shortest or least-cost path, or when there’s a risk of infinite loops without visited-state checks.

**Uniform Cost Search (UCS):**
- Best for: Weighted graph problems where path costs vary, such as transportation networks, route optimization, or resource allocation. It guarantees an optimal path considering edge costs.

- Avoid when: Costs are uniform (where BFS suffices) or when state space is very large, since UCS expands many nodes to ensure optimality.

---

## Section 2: Empirical Results

### Grid Navigation Performance

TODO: Complete after running algorithm_comparison.py

| Metric         | BFS                  | UCS (≈A*)    | Winner                             |
| -------------- | ---------------------| -------------| -----------------------------------|
| Path Length    | 5 (Simple), 9 (Maze) | 5, 9         | Tie                                |
| Nodes Explored | 8 (Simple), 17 (Maze)| 8 (S),12 (M) | UCS (A*)                           |
| Memory Usage   | 2 (Frontier)         | 3 (Frontier) | BFS (slightly lower)               |
| Execution Time | ~0.00 ms             | ~0.00–1.02 ms| BFS (simpler), UCS for large grids |


### Tree/Graph Search Performance

| Metric         | DFS                        | UCS                         | Winner            |
| -------------- | ---------------------------| --------------------------- | ----------------- |
| Solution Found | Foundpaths (A→C→E→G, etc.) | Found optimal weighted path | UCS               |
| Nodes Explored | 6–7 average                | 5–6 average                 | UCS               |
| Memory Usage   | Low                        | Moderate                    | DFS               |
| Execution Time | ~0.00 ms                   | ~0.00 ms                    | Tie (small input) |


### Key Findings

TODO: Analyze your experimental results

1. **Solution Quality:** 
UCS and BFS are optimal for their respective contexts — UCS for weighted graphs and BFS for unweighted grids. DFS sacrifices optimality for lower memory use.

2. **Efficiency:** 
A* (and UCS) explored up to 30% fewer nodes than BFS in complex mazes due to heuristic guidance. DFS was fastest but less reliable for optimal paths.

3. **Memory Usage:** 
DFS used minimal memory due to its stack-based nature. BFS and UCS consumed more memory since they maintain large frontiers.

4. **Scalability:** 
BFS node growth followed a quadratic trend (O(b^d)), while UCS’s cost-based expansions made it slower but still manageable. DFS scaled best in large but sparse trees.

---

## Section 3: Trade-offs Discussion

### Memory vs Solution Quality vs Runtime

TODO: Discuss the fundamental trade-offs

**Memory Efficiency:**
- DFS uses the least memory since it stores only one branch at a time. BFS and UCS, however, store all frontier nodes — making them more memory-intensive but more reliable for finding the shortest path.

**Solution Quality:**
- UCS and BFS guarantee optimal solutions (given non-negative or uniform costs). DFS can miss the best path entirely if the first explored branch is suboptimal.

**Runtime Performance:**
- DFS is generally the fastest in small or shallow trees since it doesn’t check all levels. BFS and UCS can take longer but ensure completeness and optimality.

### Problem Characteristics That Favor Each Algorithm

**Grid Problems:**
- BFS and A* perform best; BFS ensures the shortest path in uniform grids, while A* reduces node expansion using heuristics.

**Tree Problems:**
- DFS excels in exploring all branches deeply — ideal for backtracking, tree traversal, and recursive searches.

**Weighted Graph Problems:**
- UCS is the most effective because it accounts for varying edge costs and guarantees the least-cost route.

**Large Search Spaces:**
- DFS performs well when depth is more critical than completeness, while UCS and A* may become computationally expensive.

---

## Section 4: Real-world Applications

### Breadth-First Search Applications
- **GPS Navigation:** BFS can find the shortest path in simple, unweighted city grids or uniform road networks.
- **Social Networks:** Used to find shortest connection paths (e.g., “degrees of separation” between users).
- **Web Crawling:** Ensures complete coverage by exploring URLs level by level.

### Depth-First Search Applications
- **Maze Solving:** DFS can quickly find a path to the goal in deep mazes, especially when path length is not critical.
- **Topological Sorting:** Useful for dependency resolution in directed acyclic graphs.
- **Cycle Detection:** Efficiently detects loops in graphs using recursion and backtracking.

### Uniform Cost Search Applications
- **Route Planning:** Used in navigation systems to find cost-effective paths considering real distances or traffic.
- **Network Routing:** Ensures packets follow the least-cost route in weighted network topologies.
- **Resource Allocation:** Finds optimal distribution paths in logistics and supply chain systems.

## Conclusion

This project demonstrated that BFS, DFS, and UCS each have unique strengths depending on problem type and constraints.
BFS is ideal for unweighted and shallow search problems where completeness and optimality matter. DFS excels in memory-constrained or deep-tree exploration tasks but can return suboptimal results. UCS outperforms both in weighted scenarios by guaranteeing the least-cost path at the expense of higher memory and computational cost.

The empirical analysis confirmed theoretical expectations — A* (a heuristic-enhanced form of UCS) explored up to 30% fewer nodes than BFS while maintaining optimal results.
Ultimately, the best algorithm choice depends on the trade-off between speed, memory, and solution quality — a balance that defines intelligent search system design in real-world applications.

---

**Word Count:** [~940 words]