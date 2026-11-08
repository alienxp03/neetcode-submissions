from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data1, data2 = defaultdict(int), defaultdict(int)
        for a, b in zip(s, t):
            data1[a] += 1
            data2[b] += 1
        
        return data1 == data2