# Method 1
# Time: O(n)
# Space: O(n)

# (mc-1)*n - number of gaps between the most common characters
# mc - frequency of the most common character
# tie_ct - number of characters having the same frequency as the most common character (excluding the most common character)
# Examples:

# AAAABBBEEFFGG 3

# here X represents a space gap:

# Frame: "AXXXAXXXAXXXA"
# insert 'B': "ABXXABXXABXXA" <--- 'B' has higher frequency than the other characters, insert it first.
# insert 'E': "ABEXABEXABXXA"
# insert 'F': "ABEFABEXABFXA" <--- each time try to fill the k-1 gaps as full or evenly as possible.
# insert 'G': "ABEFABEGABFGA"
# AACCCBEEE 2

# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# insert 'A' among the gaps of chunks since it has higher frequency than 'B' ---> "CEACEACE"
# insert 'B' ---> "CEABCEACE" <----- result is tasks.length;
# AACCCDDEEE 3

# 3 identical chunks "CE", "CE CE CE" <--- this is a frame.
# Begin to insert 'A'->"CEA CEA CE"
# Begin to insert 'B'->"CEABCEABCE" <---- result is tasks.length;
# ACCCEEE 2

# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# Begin to insert 'A' --> "CEACE CE" <-- result is (c[25] - 1) * (n + 1) + 25 -i = 2 * 3 + 2 = 8
class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        c = collections.Counter(tasks)
        mc, tie_ct = c.most_common(1)[0][1], 0
        for k, v in c.most_common()[1:]:
            if v == mc:
                tie_ct += 1
            else:
                break
        
        return max(len(tasks), (mc-1)*n + mc + tie_ct)


# Method 2 max_heap
# Time: O(N*n)  where N is the number of tasks and n is the cool-off period.
# Space: O(1) ?? store heap

# Algorithm

# This is an extremely tricky problem.
# The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
# Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
# Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
# But if we schedule using most frequent first, then we have:
# 2.1: A,idle,idle,A,idle,idle,A
# 2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
# 3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.

class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':

        if n == 0:
            return len(tasks)

        hs = Counter(tasks)


        count = 0
        cycle = n + 1

        heap = []

        for k, i in hs.items():
            if i > 0:
                heapq.heappush(heap, (-i))                
        while heap:
            worktime = 0
            tmp = []
            for i in range(cycle):
                if heap:
                    tmp.append(heapq.heappop(heap))
                    worktime += 1
            for cnt in tmp:
                cnt *= -1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, -cnt)
            
            count += cycle if len(heap) > 0 else worktime

        return count


    	
