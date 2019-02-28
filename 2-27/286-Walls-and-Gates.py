



# Method 1 DFS
# Time: O(mn)
# Space: O(mn)

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    self.dfs(rooms,i,j,0)
        
        
    def dfs(self,rooms,ii,jj,dist):
        if ii<0 or jj<0 or ii>=len(rooms) or jj>=len(rooms[0]) or rooms[ii][jj]<dist :
            return
        rooms[ii][jj]=dist
        
        self.dfs(rooms,ii+1,jj,dist+1)
        self.dfs(rooms,ii-1,jj,dist+1)
        self.dfs(rooms,ii,jj+1,dist+1)
        self.dfs(rooms,ii,jj-1,dist+1)   





# Method 1 BFS
# Time: O(mn)
# Space: O(mn)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        h = len(rooms)
        w = len(rooms[0])
        
        q =[]
        for i in range(h):
            for j in range(w):
                if rooms[i][j]==0:
                    q.append((i,j))
        for row, col in q:
            dist=rooms[row][col]+1
            for dy,dx in (-1,0),(1,0),(0,1),(0,-1):
                r=row+dy
                c=col+dx
                if 0<=r<h and 0<=c<w and rooms[r][c] ==2147483647:
                    rooms[r][c]=dist
                    q.append((r,c))