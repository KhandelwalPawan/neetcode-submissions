class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for ang in strs:
            sort_ang = sorted(ang)
            key = tuple(sort_ang)
            if key not in ans:
                ans[key] = [ang]
            else:
                ans[key].append(ang)
        
        return list(ans.values())
        