class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int columns = grid[0].length;
        int count = 0;
        boolean[][] visited = new boolean[rows][columns];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    bfs(grid, i, j, visited, rows, columns);
                    count++;
                }
            }
        }
        return count;
    }

    public void bfs(char[][] grid, int i, int j, boolean[][] visited, int rows, int cols) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});          // Bug 2 fix: i,j not r,c
        visited[i][j] = true;

        int[][] directions = {{-1,0},{0,1},{1,0},{0,-1}};  // Bug 3 fix: semicolon

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];

            for (int[] dir : directions) {
                int nr = row + dir[0];       // Bug 4 fix: dir[0] not dr
                int nc = col + dir[1];       // Bug 4 fix: dir[1] not dc

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                        && !visited[nr][nc] && grid[nr][nc] == '1') {
                    queue.add(new int[]{nr, nc});   // Bug 5 fix: new int[]
                    visited[nr][nc] = true;
                }
            }
        }                                    // Bug 6 fix: closing braces
    }
}