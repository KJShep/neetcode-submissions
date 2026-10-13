class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s))+"%"
            ans+=s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        while(len(s) > 0):
            num = ""
            for c in s:
                if c != '%':
                    num += c
                else:
                    break
            intNum = int(num)
            s = s[len(num)+1:]
            ans.append(s[:intNum])
            s = s[intNum:]
        return ans
