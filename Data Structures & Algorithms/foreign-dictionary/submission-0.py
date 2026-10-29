class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        allchs = set()
        for i in range(n):
            for x in words[i]:
                allchs.add(x)
        
        # first construct the paths
        pre = {x:set() for x in list(allchs)}
        
        def compare(smallstring, bigstring):
            nonlocal pre
            n = min(len(smallstring), len(bigstring))
            for i in range(n):
                if smallstring[i] != bigstring[i]:
                    pre[bigstring[i]].add(smallstring[i])
                    return True
            if len(smallstring) > len(bigstring):
                return False
            else:
                return True

        for i in range(n):
            for j in range(i+1, n):
                smallstring = words[i]
                bigstring = words[j]
                z = compare(smallstring, bigstring)
                if not z:
                    return ""
        
        for x in pre:
            pre[x] = list(pre[x])
        
        chunique = list(pre.keys())
        visited = {ch:0 for ch in chunique}
        order = []

        def dfs(node):
            if visited[node] == 1:
                return False

            if visited[node] == 2:
                return True
            
            visited[node] = 1
            for pn in pre[node]:
                if not dfs(pn):
                    return False
            visited[node] = 2

            order.append(node)
            
            return True

        for ch in chunique:
            if not visited[ch]:
                if not dfs(ch):
                    return ""
        
        return "".join(order)
                