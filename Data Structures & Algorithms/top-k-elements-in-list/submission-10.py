class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        ans = []
        for j in range(k):
            most_frequent = max(seen, key=seen.get)
            ans.append(most_frequent)
            seen[most_frequent] = -1
        return ans
            