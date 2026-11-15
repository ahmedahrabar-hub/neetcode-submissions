class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[j].start < intervals[i].end and intervals[i].start < intervals[j].end:
                    return False
        return True