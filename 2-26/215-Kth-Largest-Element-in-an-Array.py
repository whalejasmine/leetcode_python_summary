
# Method 1 brute force
# Time: O(nlogn)
# Space: O(1)
# nums这个array的大小如果很小，那么就直接Sort返回完事，没必要整那老多没用的
# 如果k的size大于len(nums)， 


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        return nums[-k] if k<=len(nums) else nums[-len(nums)]


# Method 2 Max heap


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums=[-num for num in nums]
        heapq.heapify(nums)
        res=float('inf')
        for _ in range(k):
            res=heapq.heappop(nums)
        return -res




# Method3 Min heap
# Time: O(k)+ O(nlog(k)) add N times
# Space: O(k)

# 我们每次插入一个元素进我们的heap，只要这个元素比heap里面最小的值大，我们就把最小值pop出来，然后插入元素。
# 因为你每次pop最小元素，然后push过程中，heap都会重新把内部的数据进行整合，然后当pop和push执行完后，heap的顶端永远是最小的值，所以用上面的例子全部走完以后，我们看看最终的heap长啥样
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        import heapq
        return heapq.nlargest(k,nums)[-1]

class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        min_heap=[-float('inf')]*k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)
        return min_heap[0]


# Time: O(k)+ O((n-k)log(k)) add N times
# Space: O(k)
class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        min_heap=nums[:k]
        heapq.heapify(min_heap)
        for i in range(k,len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,nums[i])
        return min_heap[0]


# Max Heap vs. Min Heap
# 哪个算法更加好？

# Max: Time: O(n + klog(n)) | Space: O(n)
# Min: Time: O(k) + O((n-k) * logk) | Space: O(K)

# 如果考虑k无限接近n
# Max: O(n + nlog(n)) ~= O(nlogn)
# Min: O(n + logk) ~= O(n)

# 如果考虑k = 0.5n
# Max: O(n + nlogn)
# Min: O(n + nlogn)

# 如果考虑n 无限大
# Max: O(constant * n) 为什么是constant * n，参考
# Min: O(log(k) * n)



# Method4 Quick Select
# Time: O(n) worst cases O(n^2)
# Space: O(1)
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  #???? why two pointers
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)

