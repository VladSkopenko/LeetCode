from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for s in arr:
            count[s] = count.get(s, 0) + 1

        distinct = []
        for s in arr:
            if count[s] == 1:
                distinct.append(s)

        if k <= len(distinct):
            return distinct[k - 1]
        else:
            return ""
