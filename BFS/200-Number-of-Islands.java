class Solution {
    public static final int[][] DIR = {{1,0}, {0,1}, {-1,0}, {0,-1}};    
    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        
        // check out your original solution on Intellij
        //1. start with a root node
        //2. Mark all visited nodes as zero
        //3. Search for the next island
        int islands = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j< grid[0].length; j++) {
                if(grid[i][j] == '1') {
                    islands++;
                    dfs(grid, i, j);
                }
            }
        }
        return islands;
    }
    
    void dfs(char[][] grid, int r, int c) {
        int nr = grid.length;
        int nc = grid[0].length;
        
        // Base conditions are important
        if(r<0 || c<0 || r >= nr || c >= nc || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0';
        for(int[] dir: DIR) {
            // SINCE IT IS DFS IT COMES BACK AFTER EVERY STATEMENT SO WE CANNOT MODIFY R AND C
            dfs(grid, r + dir[0], c + dir[1]);
        }
        // dfs(grid, r - 1, c);
        // dfs(grid, r + 1, c);
        // dfs(grid, r, c - 1);
        // dfs(grid, r, c + 1);  
    }
    
    
}
