# Method 1 slding window
# Time: O(n) O(len(s))
# Space: O(1)?? 

class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        from collections import Counter
        dp=Counter(p)
        ds=Counter(s[:len(p)-1]). #compare this with Q567

        # Input:  #corner cases
		# s: "abab" p: "ab"

		# Output:
		# [0, 1, 2]
        ans=[]
        for start in range(len(p)-1,len(s)):
            ds[s[start]]+=1    

            if ds==dp: 
                ans.append(start-len(p)+1)
            ds[s[start-len(p)+1]]-=1
            if ds[s[start-len(p)+1]]==0:
                del ds[s[start-len(p)+1]]
        return ans





# Method 2. keep same as Q567
# Time: O(n) O(len(s))
# Space: O(1)

class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        from collections import Counter
        dp=Counter(p)
        ds=Counter(s[:len(p)])
        ans=[]
        for start in range(len(p),len(s)):
            if ds==dp: 
                ans.append(start-len(p))
            ds[s[start]]+=1    

            ds[s[start-len(p)]]-=1
            if ds[s[start-len(p)]]==0:
                del ds[s[start-len(p)]]
                
        
        return ans+[len(s)-len(p)] if ds==dp else ans