import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda pt: sqrt( (pt[0]**2)+ (pt[1]**2)) )
        
        return points[:k]