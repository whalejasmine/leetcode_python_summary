

# Method 1
# Time: O(n)
# Space: O(1)?? hashmap doen't include in the space?




from collections import Counter
class Solution:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        d1,d2=Counter(s1),Counter(s2[:len(s1)])# record s1 length char counts

        #start window from the index which substruct length s1
        
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True
            #move right +1
            d2[s2[start]] += 1
            #in order keep sliding window =len(s1)
            d2[s2[start-len(s1)]] -= 1
            # if doens't exit this element delete
            if d2[s2[start-len(s1)]] == 0: 
                del d2[s2[start-len(s1)]]
        return d1 == d2

if __name__ == "__main__":
    print (Solution().checkInclusion("ab","eidbaooo"))
    print (Solution().checkInclusion("ab","eidboaooo"))
