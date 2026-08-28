# Phase 1: Data Structures & Algorithms
**Duration:** Weeks 1–3 (3 Weeks)  
**Target WGU Course:** Real Life Applications of Data Structures (3 CUs)

---

## 1. Official WGU Competencies Covered
- [ ] Analyze challenges of integrating multiple data structures into a software product.
- [ ] Evaluate performance based on time vs. space complexity.
- [ ] Identify resources/libraries for algorithms in modern software development.
- [ ] Identify data structures appropriate for specific business and software needs.
- [ ] Implement data structures to meet software requirements effectively.

---

## 2. Comprehensive Study Topics

### 2.1 Algorithm Fundamentals
- **Core Concepts:** Definition of an algorithm, correctness proofs, efficiency metrics.
- **Asymptotic Analysis:** Big-O (upper bound), Big-Theta (tight bound), Big-Omega (lower bound).
- **Cases:** Best-case, average-case, and worst-case scenarios.
- **Trade-offs:** Time complexity vs. space complexity optimization.

### 2.2 Core Linear Data Structures
- **Arrays:** Static vs. dynamic arrays (`std::vector`, Python `list`). Insertion, deletion, access ($O(1)$ lookup, $O(n)$ search/shift).
- **Linked Lists:** Singly linked, doubly linked, and circular linked lists. Pointer manipulations, insertion/deletion overhead vs. continuous memory arrays.
- **Stacks:** LIFO operations (Push, Pop, Peek). Function call stacks, evaluation of postfix expressions, undo mechanisms.
- **Queues:** FIFO operations (Enqueue, Dequeue). Circular queues, Deques, Priority Queues (Binary Heap representation).

### 2.3 Non-Linear Data Structures & Hashing
- **Hash Tables:** Hash functions, collision resolution (Chaining with linked lists/arrays, Open Addressing with linear/quadratic probing, double hashing). Python `dict` and `set` mechanics.
- **Trees:** Terminology (root, leaf, height, depth). Binary Trees, Binary Search Trees (BST), Balanced Trees (AVL, Red-Black principles), Heaps (Min-Heap / Max-Heap).
- **Graphs:** Representations (Adjacency Matrix vs. Adjacency List). Traversals: Breadth-First Search (BFS) and Depth-First Search (DFS). Directed vs. Undirected, Weighted vs. Unweighted.

### 2.4 Searching, Sorting & Algorithmic Techniques
- **Searching:** Linear Search, Binary Search (on sorted structures), Hash-based $O(1)$ lookup.
- **Sorting:** Comparison sorts (Bubble, Selection, Insertion - $O(n^2)$; Merge, Quick, Heap - $O(n \log n)$). Non-comparison sorts (Counting, Radix).
- **Paradigms:** Recursion, Divide & Conquer, Greedy Algorithms, Dynamic Programming (Memoization & Tabulation), Backtracking.

### 2.5 Python Standard Data Structure Libraries
- `list` / `tuple` / `set` / `dict`
- `collections.deque` (Double-ended queue for fast $O(1)$ appends/pops from both ends)
- `heapq` (Min-heap implementation for priority queues)
- `queue.Queue` / `queue.PriorityQueue` (Thread-safe queues)
- `bisect` (Binary search on sorted lists)

---

## 3. Practical Trade-off & Application Scenarios

| Business / Software Scenario | Recommended Data Structure | Justification & Complexity |
| :--- | :--- | :--- |
| High-frequency key-value lookup (e.g., User session storage) | **Hash Table (`dict`)** | $O(1)$ average time complexity for lookup, insertion, and deletion. |
| Task scheduling with priority levels | **Priority Queue (`heapq`)** | $O(\log n)$ insertion and extraction of highest-priority item. |
| Breadth-First Search / Order processing queue | **Queue (`collections.deque`)** | $O(1)$ append and popleft operations; LIFO order preservation. |
| Undo/Redo history in a text editor | **Stack** | LIFO behavior naturally mirrors operation history. |
| Hierarchical data representation (File system, XML/JSON parsing) | **Tree (BST / General Tree)** | Hierarchical relationships, $O(\log n)$ search in balanced trees. |

---

## 4. Phase Deliverable
**Project:** Python Data Structure & Algorithmic Engine  
**Requirement:** Build a Python application solving a practical problem (e.g., Order Processing & Inventory Management System) that explicitly implements and integrates:
1. Dynamic Array (`list`) for sequential record keeping.
2. Stack (`list` / custom class) for operation rollback history.
3. Queue (`collections.deque`) for incoming order intake.
4. Hash Table (`dict`) for instant inventory item lookup by SKU.
5. Tree/Heap (`heapq`) for priority order dispatching based on shipping tier.

---

## 5. Weekly Schedule & Action Plan

```
Week 1: Foundations, Complexity, Arrays, Linked Lists, Stacks, & Queues
├── Mon-Tue: Algorithm definitions, Big-O analysis, Time/Space trade-offs.
├── Wed-Thu: Arrays & Linked Lists implementation and comparison.
└── Fri-Sun: Stacks & Queues: core logic, Python collections, practice problems.

Week 2: Hash Tables, Trees, & Graphs
├── Mon-Tue: Hash functions, collision resolution, Python dict internal mechanics.
├── Wed-Thu: Trees, BST implementation, Traversals (In-order, Pre-order, Post-order).
└── Fri-Sun: Heaps (`heapq`), Graphs, Adjacency Lists, BFS and DFS algorithms.

Week 3: Searching, Sorting, Algorithmic Paradigms, & Phase Project
├── Mon-Tue: Binary Search, Merge Sort, Quick Sort, Greedy vs DP basics.
├── Wed-Thu: Python built-in library practice (`collections`, `heapq`, `bisect`).
└── Fri-Sun: Build Phase Deliverable project, review WGU competencies checklist.
```

---

## 6. WGU Competency Verification Checklist
- [ ] Can explain time and space complexity of any algorithm using Big-O notation.
- [ ] Can choose between an Array and a Linked List based on insertion vs. access requirements.
- [ ] Can resolve hash collisions conceptually and build custom hash-table mechanics.
- [ ] Can write code implementing BFS/DFS on a graph structure.
- [ ] Can justify data structure selection for a specific enterprise software requirement.
