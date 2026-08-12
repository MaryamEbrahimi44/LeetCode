class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> List[List[int]]:
        top=x
        buttom=x+k-1
        while top<buttom:

            grid[top][y:y+k],grid[buttom][y:y+k]=grid[buttom][y:y+k],grid[top][y:y+k]
            top+=1
            buttom-=1
        return grid
        