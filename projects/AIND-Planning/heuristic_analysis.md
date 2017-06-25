1. Provide an optimal plan for Problems 1, 2, and 3.
  - Problems 1:
      - Load(C1, P1, SFO)
      - Load(C2, P2, JFK)
      - Fly(P2, JFK, SFO)
      - Unload(C2, P2, SFO)
      - Fly(P1, SFO, JFK)
      - Unload(C1, P1, JFK)
   - Problems 2:
      - Load(C1, P1, SFO)
      - Load(C2, P2, JFK)
      - Load(C3, P3, ATL)
      - Fly(P2, JFK, SFO)
      - Unload(C2, P2, SFO)
      - Fly(P1, SFO, JFK)
      - Unload(C1, P1, JFK)
      - Fly(P3, ATL, SFO)
      - Unload(C3, P3, SFO)
   - Problems 3:
      - Load(C1, P1, SFO)
      - Load(C2, P2, JFK)
      - Fly(P1, SFO, ATL)
      - Load(C3, P1, ATL)
      - Fly(P2, JFK, ORD)
      - Load(C4, P2, ORD)
      - Fly(P2, ORD, SFO)
      - Fly(P1, ATL, JFK)
      - Unload(C1, P1, JFK)
      - Unload(C2, P2, SFO)
      - Unload(C3, P1, JFK)
      - Unload(C4, P2, SFO)

2. Compare and contrast non-heuristic search result metrics (optimality, time elapsed, number of node expansions) for Problems 1,2, and 3. Include breadth-first, depth-first, and at least one other uninformed non-heuristic search in your comparison; Your third choice of non-heuristic search may be skipped for Problem 3 if it takes longer than 10 minutes to run, but a note in this case should be included.

3. Compare and contrast heuristic search result metrics using A* with the "ignore preconditions" and "level-sum" heuristics for Problems 1, 2, and 3.

| Problems 1           |optimality| time (sec)| #node expansions|#goal tests|
| :------------------: |:--------:| :--------:| :--------------:|:---------:|
| breadth-first        |6         | 0.028     | 43              |56         |
| depth-first          |20        | 0.016     | 21              |22         |
| uniform-cost-search  |6         | 0.037     | 55              |57         |
| ignore-preconditions |6         | 0.040     | 41              |43         |
| level-sum            |6         | 0.730     | 11              |13         |

| Problems 2           |optimality| time (sec)| #node expansions|#goal tests|
| :-----------------:  |:--------:| :--------:| :--------------:|:---------:|
| breadth-first        |3343      | 11.45     | 3343            |4609       |
| depth-first          |619       | 2.932     | 624             |625        |
| uniform-cost-search  |9         | 10.21     | 4853            |4855       |
| ignore-preconditions |9         | 3.605     | 1450            |1452       |
| level-sum            |9         | 39.89     | 86              |88         |

| Problems 3           |optimality| time (sec)| #node expansions|#goal tests|
| :------------------: |:--------:| :--------:| :--------------:|:---------:|
| breadth-first        |12        | 88.43     | 14663           |18098      |
| depth-first          |392       | 1.549     | 408             |409        |
| uniform-cost-search  |12        | 0.037     | 18151           |18153      |
| ignore-preconditions |12        | 14.31     | 5038            |5040       |
| level-sum            |12        | 202.1     | 314             |316        |
***Note: the optimality  above is defined simply based on the plan length of the solution***


4. What was the best heuristic used in these problems? Was it better than non-heuristic search planning methods for all problems? Why or why not?

In the three problems above, the ignore-precondition heuristic takes less time but more memory than level sum heuristic, while the uniform cost search seems to be the generally best searching method, and its performance was better than non-heuristic search planning methods for all problems. 

In the non-heuristic search method, the breadth first search gains more optimality than depth first search. However, in terms of the node expansions(memory complexity), the depth first search is in advantage. This results agrees with the theoretical analysis from Norvig and Russell's textbook. 

5. Provide tables or other visual aids as needed for clarity in your discussion.

More detailed results are listed in ./result.txt* with the max search time was set as 60 seconds
