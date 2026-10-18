class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            ans = []
            
            def dfs(start: int, curr: List[int]):
                # Append a copy of curr so future modifications don't affect stored results
                ans.append(list(curr))
                
                for i in range(start, len(nums)):
                    curr.append(nums[i])          # Choose
                    dfs(i + 1, curr)              # Explore (note: pass i + 1, not start + 1)
                    curr.pop()                    # Un-choose (Backtrack)
                    
            dfs(0, [])
            return ans