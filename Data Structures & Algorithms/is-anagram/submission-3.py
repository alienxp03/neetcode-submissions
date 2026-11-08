class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        dict1 =  {}
        dict2 = {}
        for c in str1:
            if c in dict1:
                dict1[c] = dict1[c] + 1
            else:
                dict1[c] = 1

        for c in str2:
            if c in dict2:
                dict2[c] = dict2[c] + 1
            else:
                dict2[c] = 1

        for key in dict1:
            if key in dict2 and dict1[key] != dict2[key]:
                return False

        return dict1 == dict2
