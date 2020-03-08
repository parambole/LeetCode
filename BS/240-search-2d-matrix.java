class Solution {
    
    
    // APPROACH - 2
    
    
    // The main idea that you need to observe is How can I convert this into BS
    // If lesser where do I go
    // If greater than where do I go
    // Where do I actually start so that this rule holds true
    
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int row = 0;
        int col = matrix[0].length - 1;
        while(row < matrix.length && col >= 0) {
            if(matrix[row][col] == target) {
                return true;
            // GO LEFT OR RIGHT BY 1 ELEMENT CORNER WALA HAI
            } else if (matrix[row][col] > target) {
                col--;
            } else if (matrix[row][col] < target) {
                row ++;
            }
        }
        return false;
    }
    
    
    
    
    
    
    
//     public boolean searchMatrix(int[][] matrix, int target) {
//         for(int[] m : matrix) {
//             if(bs(m, target) == true) return true;
//         }
//         return false;
//     }
    
//     public boolean bs(int[] m, int target) {
//         // SAME MISTAKE AS LAST TIME HIGH IS LENGTH - 1
//         int high = m.length - 1;
//         int low = 0;
//         while(low <= high) {
//             int mid = (high + low) / 2;
//             if(m[mid] == target) {
//                 return true;
//             } else if (m[mid] > target) {
//                 high = mid - 1;
//             } else {
//                 low = mid + 1;
//             }
            
//         }
//         return false;
//     }
    
    
    
    
    
    
}
