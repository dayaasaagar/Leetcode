class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()

        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    res.append((neighbor_row, neighbor_col))
            return res

        def bfs(starting_node):
            queue = deque([starting_node])
            visited.add(starting_node)
            while queue:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if grid[r][c] == '1' and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        island_count = 0

        # Iterate through the grid
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs((r, c))  # Perform BFS to mark the entire island
                    island_count += 1
        
        return island_count