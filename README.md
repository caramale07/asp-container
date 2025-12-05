# Water Container Balancer

A Python program that models interconnected water containers. When we connect two containers, the water levels equalize across all connected containers.

## The Problem

We have multiple water containers. We can connect any two containers together. When containers connect, the water redistributes so that all connected containers have the same water level.

We can also:

- Add water to any container (the water spreads to all connected containers)
- Disconnect containers (they stop sharing water)
- Connect containers that are already part of larger groups (all groups merge and equalize)

## Our Solution

We treat the containers as a graph. Each container is a node. Each connection is an edge.

When We connect two containers, we:

1. Add edges between them (bidirectional)
2. Find all containers in the connected component
3. Calculate the average water level
4. Set every container in the component to that average

When we add water, we do the same redistribution. When we disconnect, we remove the edge but keep the current water levels.

## Data Structure

Each `Container` object stores:

- `amount`: The current water level (float)
- `neighbors`: A set of connected containers

We use a set for neighbors because:

- Lookups are O(1)
- No duplicate connections
- Easy to add and remove edges

## Algorithm

**Finding connected components:**
We use depth-first search (DFS) with a stack. Start at one container, visit all neighbors, mark them as visited, and continue until we've found every container in the component.

**Avoiding redundant work:**
Before connecting two containers, we check if they're already in the same component. If they are, we skip the connection (it would create a redundant edge and waste time).

**Redistribution:**

1. Start DFS from any container in the component
2. Collect all containers into a list
3. Sum their water amounts
4. Divide by the count to get the average
5. Write the average to every container

## Complexity

- Connect: O(N + E) where N is containers and E is edges in the component
- Add water: O(N + E) for redistribution
- Disconnect: O(1) to remove edges
- Check connectivity: O(N + E) for DFS traversal


For large graphs with many operations, we could optimize with union-find and cached totals to avoid repeated traversals.

## Usage

```python
from main import Container

c1 = Container(10.0)
c2 = Container(20.0)

c1.connect(c2)

c1.add_water(10.0)  # Both now have 20.0

c1.disconnect(c2)
```

Run the tests:

```bash
python main.py
```

## Notes

- Duplicate connections are ignored
- Self-connections are ignored
- Cycle-forming connections are detected and handled as no-ops
- Disconnecting preserves current water levels
- The graph is undirected (edges go both ways)
