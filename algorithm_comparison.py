"""
Algorithm Comparison Analysis

Compare performance of BFS, DFS, and UCS on various problem types.
This script will help you analyze the trade-offs between different search algorithms.

TODO: Implement the comparison functions after completing your algorithm implementations.
"""

import sys
import os
import time
import random
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import your algorithm implementations
try:
    from bfs_grid import GridSearchBFS
    from dfs_tree import TreeNode, TreeSearchDFS
    from ucs_graph import WeightedGraphUCS
    from astar_grid import GridSearchAStar
except ImportError as e:
    print(f"Error importing algorithms: {e}")
    print("Make sure you've implemented all algorithms!")
    sys.exit(1)

def compare_grid_algorithms():
    """
    Compare BFS, A*, and grid navigation algorithms
    """
    print("Grid Algorithm Comparison")
    print("-" * 40)
    
    # Import sample problems
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'problems'))
    from sample_problems import get_simple_grid, get_maze_grid
    
    test_grids = [
        ("Simple 3x3", get_simple_grid()),
        ("Maze 5x5", get_maze_grid()),
    ]
    
    for name, (grid, start, goal) in test_grids:
        print(f"\n{name} Grid:")
        print(f"Start: {start}, Goal: {goal}")
        
        results = {}
        
        # Test BFS (if implemented)
        try:
            bfs = GridSearchBFS(grid, start, goal)
            start_time = time.time()
            path, nodes, frontier = bfs.breadth_first_search()
            bfs_time = time.time() - start_time
            
            results['BFS'] = {
                'path_length': len(path) if path else None,
                'nodes_explored': nodes,
                'max_frontier': frontier,
                'time': bfs_time * 1000  # ms
            }
        except:
            results['BFS'] = {'error': 'Not implemented or failed'}
        
        # Test A* with different heuristics
        heuristics = ['manhattan', 'euclidean']
        for h in heuristics:
            try:
                astar = GridSearchAStar(grid, start, goal, h)
                start_time = time.time()
                path, nodes, frontier = astar.astar_search()
                astar_time = time.time() - start_time
                
                results[f'A*-{h}'] = {
                    'path_length': len(path) if path else None,
                    'nodes_explored': nodes,
                    'max_frontier': frontier,
                    'time': astar_time * 1000  # ms
                }
            except:
                results[f'A*-{h}'] = {'error': 'Failed'}
        
        # Print comparison table
        print(f"{'Algorithm':<12} {'Path':<6} {'Nodes':<8} {'Frontier':<9} {'Time(ms)':<10}")
        print("-" * 55)
        
        for alg, data in results.items():
            if 'error' in data:
                print(f"{alg:<12} {data['error']}")
            else:
                path_len = data['path_length'] if data['path_length'] else 'None'
                print(f"{alg:<12} {str(path_len):<6} {data['nodes_explored']:<8} "
                      f"{data['max_frontier']:<9} {data['time']:<10.2f}")
        
        # Analysis
        if 'BFS' in results and 'A*-manhattan' in results:
            if (not 'error' in results['BFS'] and not 'error' in results['A*-manhattan']):
                bfs_nodes = results['BFS']['nodes_explored']
                astar_nodes = results['A*-manhattan']['nodes_explored']
                improvement = ((bfs_nodes - astar_nodes) / bfs_nodes) * 100
                print(f"\nA* Efficiency: {improvement:.1f}% fewer nodes than BFS")
    
    print()

def compare_graph_algorithms():
    """
    Compare all three algorithms on graph problems
    """
    print("Graph Algorithm Comparison")
    print("-" * 40)
    
    # TODO: Implement graph comparison
    # 1. Create graph problems (trees for DFS, weighted graphs for UCS)
    # 2. Run each algorithm on appropriate problems
    # 3. Compare solution quality, efficiency, memory usage
    
    print("TODO: Implement graph algorithm comparison")
    print("You'll compare DFS vs UCS on graph search problems")
    print()

        # Define weighted graph for UCS
    weighted_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 3), ('D', 5)],
        'C': [('D', 2)],
        'D': []
    }
    
    # Define tree for DFS
    root = TreeNode('A')
    b, c = TreeNode('B'), TreeNode('C')
    d, e, f = TreeNode('D'), TreeNode('E'), TreeNode('F')
    root.children = [b, c]
    b.children = [d]
    c.children = [e, f]
    
    results = {}
    
    # --- DFS ---
    try:
        dfs = TreeSearchDFS(root, target='D')  # target set here
        start_time = time.time()
        path, nodes_explored = dfs.depth_first_search()  
        dfs_time = (time.time() - start_time) * 1000
        results['DFS'] = {
            'path_length': len(path) if path else None,
            'nodes_explored': nodes_explored,
            'time': dfs_time
        }
    except Exception as e:
        results['DFS'] = {'error': str(e)}
    
    # --- UCS ---
    try:
        ucs = WeightedGraphUCS(weighted_graph)
        start_time = time.time()
        path, cost, nodes_explored, _ = ucs.uniform_cost_search('A', 'D')
        ucs_time = (time.time() - start_time) * 1000
        results['UCS'] = {
            'path_length': len(path) if path else None,
            'total_cost': cost,
            'nodes_explored': nodes_explored,
            'time': ucs_time
        }
    except Exception as e:
        results['UCS'] = {'error': str(e)}
    
    # --- Print results ---
    print(f"{'Algorithm':<10} {'PathLen':<8} {'Nodes':<8} {'Cost':<8} {'Time(ms)':<10}")
    print("-" * 50)
    for alg, data in results.items():
        if 'error' in data:
            print(f"{alg:<10} {data['error']}")
        else:
            cost = data.get('total_cost', '-')
            print(f"{alg:<10} {data['path_length']:<8} {data['nodes_explored']:<8} {cost:<8} {data['time']:<10.2f}")
    print()


def analyze_complexity():
    """
    Analyze time and space complexity empirically
    """
    print("Complexity Analysis")
    print("-" * 40)
    
    # TODO: Implement complexity analysis
    # 1. Create problems of increasing size
    # 2. Measure time and space usage for each algorithm
    # 3. Plot results to verify theoretical complexity
    
    print("TODO: Implement complexity analysis")
    print("You'll measure how algorithms scale with problem size")
    print()

    problem_sizes = [5, 10, 15, 20, 25, 30, 35, 40]
    results = []
    
    for size in problem_sizes:
        print(f"\nAnalyzing problem size: {size}")
        
        # BFS grid
        grid = [[0]*size for _ in range(size)]
        start, goal = (0,0), (size-1, size-1)
        bfs = GridSearchBFS(grid, start, goal)
        start_time = time.time()
        path, nodes, frontier = bfs.breadth_first_search()
        bfs_time = (time.time() - start_time) * 1000
        
        # DFS tree
        def build_tree(depth):
            if depth == 0:
                return None
            node = TreeNode(f"N{depth}")
            node.children = [build_tree(depth-1), build_tree(depth-1)]
            node.children = [c for c in node.children if c]
            return node
        root = build_tree(size//2)
        dfs = TreeSearchDFS(root, f"N1")
        start_time = time.time()
        path, dfs_nodes, max_depth = dfs.depth_first_search()
        dfs_time = (time.time() - start_time) * 1000
        
        # UCS weighted graph
        graph = {}
        for i in range(size):
            node = chr(65+i)
            graph[node] = []
            if i+1<size:
                graph[node].append((chr(65+i+1), random.randint(1,5)))
        ucs = WeightedGraphUCS(graph)
        start_time = time.time()
        path, cost, ucs_nodes, frontier = ucs.uniform_cost_search('A', chr(65+size-1))
        ucs_time = (time.time() - start_time) * 1000
        
        results.append({
            'size': size,
            'BFS_nodes': nodes,
            'BFS_time': bfs_time,
            'DFS_nodes': dfs_nodes,
            'DFS_time': dfs_time,
            'UCS_nodes': ucs_nodes,
            'UCS_time': ucs_time
        })
    
    # Print table
    print(f"\n{'Size':<6} {'BFS_nodes':<10} {'BFS(ms)':<10} {'DFS_nodes':<10} {'DFS(ms)':<10} {'UCS_nodes':<10} {'UCS(ms)':<10}")
    print("-"*70)
    for r in results:
        print(f"{r['size']:<6} {r['BFS_nodes']:<10} {r['BFS_time']:<10.2f} "
              f"{r['DFS_nodes']:<10} {r['DFS_time']:<10.2f} {r['UCS_nodes']:<10} {r['UCS_time']:<10.2f}")
    
    # Plot nodes expanded
    sizes = [r['size'] for r in results]
    plt.figure(figsize=(8,5))
    plt.plot(sizes, [r['BFS_nodes'] for r in results], 'o-', label='BFS Nodes')
    plt.plot(sizes, [r['DFS_nodes'] for r in results], 's-', label='DFS Nodes')
    plt.plot(sizes, [r['UCS_nodes'] for r in results], '^-', label='UCS Nodes')
    plt.xlabel("Problem Size")
    plt.ylabel("Nodes Expanded")
    plt.title("Node Expansion Complexity")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    output_dir = os.path.join(os.path.dirname(__file__), "analysis")
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "bfs_dfs_ucs_nodes.png"))
    plt.show()
    
    # Plot execution time
    plt.figure(figsize=(8,5))
    plt.plot(sizes, [r['BFS_time'] for r in results], 'o-', label='BFS Time')
    plt.plot(sizes, [r['DFS_time'] for r in results], 's-', label='DFS Time')
    plt.plot(sizes, [r['UCS_time'] for r in results], '^-', label='UCS Time')
    plt.xlabel("Problem Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Time Complexity Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "bfs_dfs_ucs_time.png"))
    plt.show()
    
    print("- UCS behaves like BFS but weighted; grows faster with cost updates.")
    print("Plots confirm empirical trends.")


def generate_report():
    """
    Generate comparison report for analysis document
    """
    print("Algorithm Comparison Report")
    print("=" * 50)
    
    print("\n1. GRID NAVIGATION RESULTS:")
    compare_grid_algorithms()
    
    print("2. GRAPH SEARCH RESULTS:")
    compare_graph_algorithms()
    
    print("3. COMPLEXITY ANALYSIS:")
    analyze_complexity()
    
    print("4. SUMMARY AND RECOMMENDATIONS:")
    print("-" * 40)
    print("Algorithm Selection Guide:")
    print("- BFS: Best for unweighted shortest paths, guaranteed optimal")
    print("- DFS: Best for memory-constrained tree traversal")
    print("- UCS: Best for weighted optimal pathfinding") 
    print("- A*: Best for pathfinding with good heuristics, most efficient")
    print("\nKey Insights:")
    print("- A* typically explores fewer nodes than BFS while finding optimal paths")
    print("- Manhattan distance is best heuristic for 4-connected grids")
    print("- All informed search algorithms require admissible heuristics for optimality")
    print()
    
    print("Use these results to complete your analysis report!")

if __name__ == "__main__":
    print("Search Algorithm Performance Comparison")
    print("=" * 60)
    print("This script compares BFS, DFS, and UCS performance.")
    print("Complete your algorithm implementations first!")
    print()
    
    generate_report()