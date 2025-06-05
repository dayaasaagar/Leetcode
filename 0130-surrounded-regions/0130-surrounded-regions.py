class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        rows,cols = len(board),len(board[0])



        def bfs(x,y):

            queue = deque([(x,y)])




            while queue:
                x,y = queue.popleft()
                board[x][y] = 'T'
                
                directions =[(-1,0),(0,-1),(1,0),(0,1)]



                for dr,dc in directions:
                    nr,nc = dr+x,y+dc

                    if nr>=0 and nr<rows and nc>=0 and nc<cols and board[nr][nc]=='O':
                        board[nr][nc]='T'
                        queue.append((nr,nc))

                

            



        for i in range(rows):

            if board[i][0] =='O':
                bfs(i,0)
            if board[i][cols-1]=='O':
                bfs(i,cols-1)

        for j in range(cols):

            if  board[0][j] == 'O':
                bfs(0,j)
            if board[rows-1][j]=='O':
                bfs(rows-1,j)
        
        for i in range(rows):
            for j in range(cols):

                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j] == 'T':
                    board[i][j]='O'



        




