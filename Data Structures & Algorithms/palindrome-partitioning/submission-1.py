class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        res = []
        n = len(s)
        
        def dfs(start,curpath):

            if start == n:
                res.append(curpath.copy())
                return
            
            for end in range(start + 1, n + 1):
                
                substring = s[start: end]

                if substring == substring[::-1]:
                    curpath.append(substring)
                    dfs(end, curpath)
                    curpath.pop()
        dfs(0,[])
        return res