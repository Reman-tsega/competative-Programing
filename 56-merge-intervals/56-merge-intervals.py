class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_list=[]
        new_list.append(intervals[0])
        for i in range(1,len(intervals)):
            if new_list[-1][1]>=intervals[i][0]:
                if new_list[-1][-1]<intervals[i][1]:
                    new_list[-1][1]=intervals[i][1]
            else:
                new_list.append(intervals[i])
        return new_list
                
                
        