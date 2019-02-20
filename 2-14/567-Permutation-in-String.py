

# Method 1
# Time: O(n)
# Space: O(1)?? hashmap doen't include in the space?




from collections import Counter
class Solution1:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        d1,d2=Counter(s1),Counter(s2[:len(s1)])# record s1 length char counts

        #start window from the index which substruct length s1
        
        for start in range(len(s1), len(s2)):
            #always check the two dictriony first 
            if d1 == d2: return True
            #s2 pointer sliding window move right +1
            d2[s2[start]] += 1
            #in order keep sliding window =len(s1)
            d2[s2[start-len(s1)]] -= 1
            # keep length
            if d2[s2[start-len(s1)]] == 0: 
                del d2[s2[start-len(s1)]]
        return d1 == d2



# Method 2 Brute Force
# Time: O(n！)  n is the length of s1
# Space: O(n^2) The depth of the recursion tree is n.
# n refers to the length of the short string s1). Every node of the recursion tree contains a string of max. length n.
class Solution2:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':


# Method 3 Sorting
# Time: O(l1log(l1)+(l2-l1)l1log(l2))  where l1 is the length of string l1 and l2 is the length of string l2.
# Space: O(l1). t array is used.



class Solution3:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':




if __name__ == "__main__":
    print (Solution().checkInclusion("ab","eidbaooo"))
    print (Solution().checkInclusion("ab","eidboaooo"))
