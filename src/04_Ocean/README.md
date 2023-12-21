### Ocean


Model the oceanic system in which fish and shrimp live. The ocean is represented
by a two-dimensional array of cells. Each cell can be empty, or it can contain
a rock, fish or shrimp. In any time quantum, some cells can change (only cells with rocks do not change with time).


Fish exist according to the cellular automata rules of life: if a fish has cramped (from 4 or more fish neighbors), or too lonely (no more than one neighbor of fish), then the fish dies in the next time quantum.
If the fish have 2 or 3 neighbor fish, the fish simply continues to live. In the empty cell a new fish appears, if it has exactly 3 fish neighbors.
Shrimps exist by the same rules. If an empty cell has exactly 3 fish neighbor and 3 shrimp neighbors, then one fish is born.
The workpiece and interface that you need to implement you will find in the file `ocean.py`.

**Input:**
```bash
$ python3 ocean.py < input.txt

```
or 
```
1          
5 5        
0 2 0 1 3  
0 2 0 3 3  
0 2 2 2 1  
2 1 2 0 3  
3 3 1 3 3  

```

**Output:**
```
0 0 0 1 3
2 2 0 3 3
2 0 0 2 1
0 1 2 2 3
0 0 1 3 3
```

