
class Solution:
	def maxResult(self, A: List[int], k: int) -> int:
		log = deque([(0, -k)])
		for i, a in enumerate(A):
			if i - log[0][1] > k:
				log.popleft()
			a += log[0][0]
			while log and log[-1][0] <= a:
				log.pop()
			log.append((a, i))
		return a