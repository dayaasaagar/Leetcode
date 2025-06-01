class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {


        int rows = matrix.length;
        int cols = matrix[0].length;
        List<Integer> result = new ArrayList<>();

        int top =0;
        int bottom = rows-1;
        int left = 0;
        int right = cols-1;
        while(top<=bottom && left<=right)
        {
            for(int i=left;i<=right;i++){
                result.add(matrix[top][i]);

            }
            top++;
            for(int j=top;j<=bottom;j++){
                result.add(matrix[j][right]);
            }
            right--;
          if(top<=bottom){
              for(int k=right;k>=left;k--)
            {
                result.add(matrix[bottom][k]);
            }
            bottom--;
          }
          if(left<=right){
            for(int m =bottom;m>=top;m--)
            {
                result.add(matrix[m][left]);
            }
            left++;
          }
            
        }
        return result;
        
    }
}