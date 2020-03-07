class Solution {
    
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int count_fresh = 0;
        //Put the position of all rotten oranges in queue
        //count the number of fresh oranges
        for(int i = 0 ; i < rows ; i++) {
            for(int j = 0 ; j < cols ; j++) {
                if(grid[i][j] == 2) {
                    queue.offer(new int[]{i , j});
                }
                else if(grid[i][j] == 1) {
                    count_fresh++;
                }
            }
        }
        //if count of fresh oranges is zero --> return 0 
        if(count_fresh == 0) return 0;
        int count = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        //bfs starting from initially rotten oranges
        while(!queue.isEmpty()) {
            ++count;
            int size = queue.size();
            for(int i = 0 ; i < size ; i++) {
                int[] point = queue.poll();
                for(int dir[] : dirs) {
                    int x = point[0] + dir[0];
                    int y = point[1] + dir[1];
                    //if x or y is out of bound
                    //or the orange at (x , y) is already rotten
                    //or the cell at (x , y) is empty
                        //we do nothing
                    if(x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] == 0 || grid[x][y] == 2) continue;
                    //mark the orange at (x , y) as rotten
                    grid[x][y] = 2;
                    //put the new rotten orange at (x , y) in queue
                    queue.offer(new int[]{x , y});
                    //decrease the count of fresh oranges by 1
                    count_fresh--;
                }
            }
        }
        return count_fresh == 0 ? count-1 : -1;
    }
    
    
    
//     public int orangesRotting(int[][] grid) {
//         Queue<Point> queue = new LinkedList<>();
//         int fresh = 0;
//         for(int i = 0; i < grid.length; i++) {
//             for(int j = 0; j < grid[0].length; j++) {
//                 if(grid[i][j] == 2) {
//                     queue.add(new Point(i,j));
//                 } else if(grid[i][j] == 1) {
//                     fresh++;
//                 }
//             }
//         }
//         if(fresh == 0) return 0;
//         int step = 1;
//         while(!queue.isEmpty()) {
//             for(int i = queue.size(); i >= 0; i--) {
//                 Point p = queue.poll();
//                 for(int[] dir : DIR) {
//                     int r = p.r + dir[0];
//                     int c = p.c + dir[1];
//                     if(isSafe(r,c,grid)) {
//                         grid[r][c] = 2;
//                         queue.add(new Point(r,c));
//                         fresh--;
//                     }
//                 }
//             }
//         }
        
//         return fresh == 0 ? step: -1;
//     }
    
//     public static boolean isSafe(int r, int c, int[][] grid) {
//         if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 2 || grid[r][c] == 0) {
//             return false;
//         }
//         return true;
//     }
    
//     public static int[][] DIR = {{1,0},{-1,0},{0,1},{0,-1}};
    
//     static class Point {
//         int r;
//         int c;
//         Point(int r, int c) {
//             this.r = r;
//             this.c = c;
//         }
//     }
}
