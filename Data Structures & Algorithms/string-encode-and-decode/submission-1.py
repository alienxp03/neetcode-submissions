class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            size = len(st)
            encoded = encoded + str(size) + '#' + st

        return encoded

    def decode(self, s: str) -> List[str]:
        answer = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            answer.append(s[i:j])
            i = j
        return answer