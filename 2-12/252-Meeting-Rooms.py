# Time: O(nlogn)
# Space:O(1)

# Given an array of meeting time intervals consisting of start 
# and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
class Solution:
    def canAttendMeetings(self, intervals: 'List[Interval]') -> 'bool':
        intervals.sort(key=lambda x:x.start)
        
        for i in range(1,len(intervals)):
            if intervals[i].start <intervals[i-1].end:
                return False
        return True

if __name__ == "__main__":
    print (Solution1().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20), Interval(15,18)]))