class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        n = len(words)
        
        allch = set()
        for w in words:
            for ch in w:
                allch.add(ch)

        pre = {ch:set() for ch in allch}

        def precollect(smallword, bigword):
            n = min(len(smallword), len(bigword))
            for i in range(n):
                if smallword[i] != bigword[i]:
                    pre[bigword[i]].add(smallword[i])
                    return True
            if len(smallword) > len(bigword):
                return False
            return True
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                small = words[i]
                big = words[j]
                z = precollect(small, big)
                if not z:
                    return ""

        allch = list(allch)
        visited = {x:0 for x in allch}
        
        order = []

        def dfs(ch):
            
            if visited[ch] == 1:
                return False
            if visited[ch] == 2:
                return True
            
            visited[ch] = 1
            for prex in pre[ch]:
                if not dfs(prex):
                    return False
            visited[ch] = 2
            order.append(ch)

            return True
        
        for ch in allch:
            if visited[ch] == 0:
                z = dfs(ch)
                if not z:
                    return ""

        return "".join(order)