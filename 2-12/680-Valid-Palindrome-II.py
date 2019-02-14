# Method 1
# Time: O(n)
# Space: O(n)

class Solution:
    def validPalindrome(self, s: 'str') -> 'bool':
        left,right=0,len(s)-1
        while left<right: #end and start stop condition
            if s[left]!=s[right]:
                one, two = s[left:right], s[left+1 :right + 1]
             

                #not move== reverse or move one step shound equal to reverse
                return one ==one[::-1] or two ==two[::-1]
            left, right = left+1, right-1
        return True


if __name__ == "__main__":
    print (Solution().validPalindrome("aba"))
    print (Solution().validPalindrome("abca"))
    print (Solution().validPalindrome("eeeeeeew"))