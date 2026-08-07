class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        bins = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                binr = i//3
                binc = j//3
                if value == ".":
                    continue
                if (value in rows[i]) | (value in cols[j]) | (value in bins[(binr,binc)]):
                    return False
                rows[i].add(value)
                cols[j].add(value)
                bins[(binr,binc)].add(value)
        return True