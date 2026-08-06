class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for strr in strs:
            str1 = "".join(sorted(strr))
            if str1 in group:
                group[str1].append(strr)
            else:
                group[str1] = [strr]
        return list(group.values())