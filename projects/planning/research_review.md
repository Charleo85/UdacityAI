<center>Review on the Multi-Agent A* for Parallel and Distributed Systems by Raz Nissim and Ronen Brafman [link](https://www.cs.bgu.ac.il/~raznis/mafs.pdf) </center>

#### Introduction
The main contribution of this paper is a multi-agent formulation of A* with exploration of the parallel nature of the system: the distinction between local and globally relevant actions and propositions to focus the work of each agent, dividing both states and operators among the agents, and exploiting symmetries that arise from the multi-agent structure. Both a parallel and distributed algorithm is proposed. The parallel version and achieve super-linear speedup, while the distributed version ensures that private information is not shared among agents. 

To parallelize the search, the task division and the message sending between different node is necessary. The author described in detailed how such mechanism would work. A termination detection is also implemented so that a solution is known to be optimal only if all agents prove it so.
#### Conclusion
The author also provides the proof of optimality that its Multi-Agent A* algorithm could achieve. The experiment results showed that in planning domains in which the agents are loosely-coupled, the parallel version Multi-Agent A* algorithm overwhelmingly dominates centralized A*, and efficiency decreased in these tightly- coupled systems. For the distributed version, in the tightly-coupled domains, there is a sublinear efficiency values, while in the loosely-coupled domains, it exhibits nearly linear and super-linear speedup.

<center>Review on the first chapter of Planning Algorithm by Steven M. LaValle</center>

#### Basic Ingredients of Planning
- State
- Time
- Actions
- Initial and goal states
- Feasibility&Optimality criterion

#### Search Methods
- BFS
- DFS
- Dijkstra’s algorithm
- A-star with  heuristic estimate of the cost
- Best first search, greedy approach with an priority queue is sorted according to an estimate of the optimal cost-to-g, 
- Iterative deepening, is usually preferable if the search tree has a large branching factor
- Backward search
- Bidirectional search

#### A Unified View of the Search Methods
- Initialization
- Select Vertex
- Apply an Action
- Insert a Directed Edge into the Graph
- Check for Solution
- Return to Step 2

#### Historical Development
- The problem space: Totally ordered action sequences ->  interleaving of actions from different subplans within a single sequence -> interleaving of actions from different subplans with potential conflicts  -> large planning problems
- The methodology: linear planning(Sacerdoti, 1975) -> goal-regression planning(Waldinger, 1975) -> partial-order planning(Tate, 1975a), (Sussman, 1975) -> state-space planning(Drew McDer- mott’s UNPOP program, 1996)
- The representation language: Action Description Language(Pednault, 1986) -> Problem Domain Description Language(Ghallab et al., 1998) -> binary decision diagrams (Clarke and Grumberg, 1987; McMillan, 1993),  Cimatti et al. (1998), Vossen et al. (2001)
