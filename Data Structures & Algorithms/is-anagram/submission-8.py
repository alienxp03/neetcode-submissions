from collections import defaultdict, Counter

class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        # dict1, dict2 = defaultdict(int), defaultdict(int)
        # for i in range(len(str1)):
        #     dict1[str1[i]] += 1
        #     dict2[str2[i]] += 1
        # return dict1 == dict2
        # return Counter(str1) == Counter(str2)
        return sorted(str1) == sorted(str2)