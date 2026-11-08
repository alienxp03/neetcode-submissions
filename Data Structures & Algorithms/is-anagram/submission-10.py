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
        # return sorted(str1) == sorted(str2)
        # print(ord('a'))
        counts = [0] * 26
        base = ord('a')
        for ch1, ch2 in zip(str1, str2):
            # print(f"ch1: {ch1} - {ord(ch1)}, ch2: {ch2} - {ord(ch2)}")
            counts[ord(ch1) - base] += 1
            counts[ord(ch2) - base] -= 1
        return all(x == 0 for x in counts)