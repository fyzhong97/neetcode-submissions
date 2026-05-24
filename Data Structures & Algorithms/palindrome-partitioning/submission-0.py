class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        res = []
        n = len(s)
        
        def dfs(start,curpath):

            if start == n:
                res.append(curpath.copy())
                return
            
            for end in range(start, n):
                
                substring = s[start:end + 1]

                if substring == substring[::-1]:
                    curpath.append(substring)
                    dfs(end + 1, curpath)
                    curpath.pop()
        dfs(0,[])
        return res