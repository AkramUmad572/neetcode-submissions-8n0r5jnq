class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1 or not intervals:
            return intervals

        copy = intervals.copy()
        copy.sort()
        new = []

        prev = copy[0]
        for overlap in range(1, len(copy)):
            if prev[1] >= copy[overlap][0] and prev[0] <= copy[overlap][1]:
                prev = [min(copy[overlap][0], prev[0]), max(copy[overlap][1], prev[1])]
            else:
                new.append(prev)
                prev = copy[overlap]
        
        new.append(prev)
        return new