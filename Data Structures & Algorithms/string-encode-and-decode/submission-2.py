class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""

        for word in strs:
            encoded_strs += f"{len(word)}##{word}"
        print(encoded_strs)
        return encoded_strs;

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        size = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == "##":
                print(size)
                end = i+int(size)
                decoded_strs.append(s[i+2:end+2])
                i = end +1
                size = ""
            else:
                size += s[i]
            i += 1
        return decoded_strs;
