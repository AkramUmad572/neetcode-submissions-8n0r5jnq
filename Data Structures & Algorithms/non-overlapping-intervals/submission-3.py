class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        non = 0

        new = intervals.copy()
        new.sort()
        prev = new[0]
        for clip in range(1, len(new)):
            if prev[1] > new[clip][0]:
                non += 1
                prev = [min(new[clip][0], prev[0]), min(new[clip][1], prev[1])]
            else:
                prev = new[clip]
        return non
