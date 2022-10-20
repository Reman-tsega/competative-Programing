class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) <= k:
            return sum(cardPoints)

        points = cardPoints[len(cardPoints) - k:] + cardPoints[:k]
        temp_sum = sum(points[:k])
        largest = temp_sum
        for i in range(len(points) - k):
            temp_sum -= (points[i] - points[i + k])
            largest = max(largest, temp_sum)
        return largest
        