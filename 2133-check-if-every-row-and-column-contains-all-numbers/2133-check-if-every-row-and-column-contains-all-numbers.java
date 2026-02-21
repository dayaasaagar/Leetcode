class Solution {
    public boolean checkValid(int[][] matrix) {
        int n = matrix.length;
        boolean[][] row = new boolean[n][n + 1];
        boolean[][] col = new boolean[n][n + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int value = matrix[i][j];

                if (value < 1 || value > n) {
                    return false;
                }

                if (row[i][value] || col[j][value]) {
                    return false;
                }

                row[i][value] = true;
                col[j][value] = true;
            }
        }

        return true;
    }
}