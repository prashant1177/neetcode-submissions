class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        for s in strs:
            sorted_text = ''.join(sorted(s))

            if sorted_text not in dicts:
                dicts[sorted_text] = []

            dicts[sorted_text].append(s)
        
        return list(dicts.values())
            
