import sys
class Solution:
    
    def cut_pos(self,queens,rank,pos):
        # 剪枝程序，每加入一个皇后，剪掉不能用的位置
        # pos:(1,2)
        # print('old_queens:'+str(queens))
        new_queens = queens.copy()
        # print('pos:'+str(pos))
        try:
            new_queens[pos[0]] = self.sub_str(new_queens[pos[0]],pos[1])
            # print('new_queens:'+str(new_queens))
        except:
            print(pos)
            print(new_queens)
        new_rank = []
        for r in rank:
            if r[0]==pos[0] or r[1]==pos[1]:
                continue
            elif r[1]<pos[1] and r[0]+r[1]==pos[1]+pos[0]:
                continue
            elif r[1]>pos[1] and r[0]-r[1]==pos[0]-pos[1]:
                continue
            else:
                new_rank.append(r)
        # print('new_rank:'+str(new_rank))
        return new_rank,new_queens
    
    def backtracking(self,queens,rank,row):
        if not rank:
            # print()
            # print('final_queens:'+str(queens))
            # q = list(map(lambda x: ''.join(x),queens))
            q_str = ''.join(queens)
            # print('long:'+q_str)
            if q_str.count('Q') == self.n:
                self.solution.append(queens)
                return
            else:
                return None  
        for pos in rank:
            if pos[0]>row+1:
                return None
            new_rank,new_queens = self.cut_pos(queens,rank,pos)
            
            self.backtracking(new_queens,new_rank,pos[0])
                
    def sub_str(self,string,num):
        l = list(string)
        l[num] = 'Q'
        return ''.join(l)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = ['.'*n]*n
        rank = []
        for i in range(n):
            for j in range(n):
                rank.append((i,j))
        self.n = n
        self.solution = []

        self.backtracking(queens,rank,-1)
        return self.solution
        
        
if __name__ == "__main__":
    n = int(sys.argv[-1])
    solutions = Solution().solveNQueens(n)
    print('solutions:'+str(solutions))