class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        prev = newInterval
        for i in intervals:
            if i[1] >= prev[0] and i[0] <= prev[1]:
                prev = [min(prev[0], i[0]), max(prev[1], i[1])]
            elif i[0] > prev[1]:
                new.append(prev)
                prev = i
            else:
                new.append(i)
        new.append(prev)
        
        return new


# temp = [min(new[0][0], new[1][0]), max(new[0][1], new[1][1])]
