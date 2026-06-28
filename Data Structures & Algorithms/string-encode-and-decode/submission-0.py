class Solution:

    # contains characters not numbers so we can use numbers to seperate the texts

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = f"{len(s):05}" # padding the length of string to 5 numbers
            out += l + s
        
        print(out)
        return out




    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            l = int(s[i:i+5])
            i = i + 5
            strs.append(s[i:i+l])
            i = i + l


        print(strs)
        return strs
