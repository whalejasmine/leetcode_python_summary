# Method 1
# Time:  O(n)
# Space: O(1)


class Solution1:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        p=1
        n=len(nums)
        output=[]
        for i in range(0,n):
            output.append(p)
            print ("output1:",output)
            p=p*nums[i]
            print ("p1:",p)
        p=1
        for i in range(n-1,-1,-1):
            output[i]=output[i]*p
            print ("output2:",output)
            p=p*nums[i]
            print ("p2:",p)
        return output
if __name__ == "__main__":
    print (Solution1().productExceptSelf([1, 2, 3,4]))





# Method 2 brute force
# Time:  O(n^2)
# Space: O(1)


class Solution2:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':

        return [reduce(lambda x,y: x*y,nums[:i]+nums[i+1:]) for i in range(len(nums))]
if __name__ == "__main__":
    print (Solution2().productExceptSelf([1, 2, 3,4]))