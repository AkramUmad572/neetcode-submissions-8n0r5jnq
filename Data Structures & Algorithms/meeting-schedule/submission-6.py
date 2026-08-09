"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        overlap = intervals.copy()
        overlap.sort(key=lambda x: x.start)
        for conflict in range(1, len(overlap)):
            if overlap[conflict].start < overlap[conflict - 1].end:
                return False
        return True