# Method 1 DFS
# Time: O(mn)+O(m)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        visited_accounts=[False]*len(accounts)
        emails_accounts_map=defaultdict(list)
        res=[]
        
        for i, account in enumerate(accounts):
            for j in range(1,len(account)):
                email=account[j]
                emails_accounts_map[email].append(i)
        def dfs(i,emails):
            if visited_accounts[i]:
                return
            visited_accounts[i]=True
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor,emails)
        
        for i,account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name,emails=account[0],set()
            dfs(i,emails)
            res.append([name]+sorted(emails))
        return res







