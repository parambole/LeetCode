class Solution {
    int n;
    int k; // This is the size of the subset
    List<List<Integer>> output = new ArrayList<>();
      public List<List<Integer>> subsets(int[] nums) {
        n = nums.length;
        for (k = 0; k <= n; ++k) {
          backtrack(0, new ArrayList<Integer>(), nums);
        }
        return output;
      }
    
    public void backtrack(int first, List<Integer> curr, int[] nums) {
        // This is to check if we have reached the length of that subset
        if(curr.size() == k ) output.add(new ArrayList(curr));
            
        // We dont have to go back because [1,2] is the same as [2,1] order does not matter
        for(int i = first; i < n; i++) {
            
            // This is to add the head
            curr.add(nums[i]);
            
            // THIS IS IMP ITS i+1 not first + 1
            backtrack(i+1, curr, nums);

            // This is to remove the last element [1,2] -> [1] so that we can do [1,3]
            curr.remove(curr.size() -1);
        }
    }
}
