
# Time:  O(n)
# Space: O(1)
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res,carry='',0
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            curval=(i>=0 and a[i]=='1') +(j>=0 and b[j]=='1')

            sum=curval+carry
            carry,rem=sum//2,sum%2
            
            res=str(rem)+res
            
            i-=1
            j-=1
        return res