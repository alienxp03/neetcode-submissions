class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        countStr1, countStr2 = {}, {}

        for i in range(len(str1)):
            countStr1[str1[i]] = 1 + countStr1.get(str1[i], 0)
            countStr2[str2[i]] = 1 + countStr2.get(str2[i], 0)

        return countStr1 == countStr2
