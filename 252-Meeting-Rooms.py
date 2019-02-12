# Time: O(nlogn)
# Space:O(1)

# Given an array of meeting time intervals consisting of start 
# and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: 'List[Interval]') -> 'bool':
        intervals.sort(key=lambda x:x.start)
        
        for i in range(1,len(intervals)):
            if intervals[i].start <intervals[i-1].end:
                return False
        return True