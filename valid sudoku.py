class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        seen = []
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val != ".":
                    row_info = f"row {r} has {val}"
                    col_info = f"col {c} has {val}"
                    box_info = f"box {r//3}-{c//3} has {val}"
                
                    if row_info in seen or col_info in seen or box_info in seen:
                        return False
                    seen.append(row_info)
                    seen.append(col_info)
                    seen.append(box_info)
        
        return True
