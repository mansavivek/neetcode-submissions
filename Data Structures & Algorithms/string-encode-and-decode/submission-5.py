class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "emptyObject"
        encodedStr = "~".join(strs)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = s.split('~')
        if decodedStrs[0] == "emptyObject":
            return []
        return decodedStrs
