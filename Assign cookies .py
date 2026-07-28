class Solution:

    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child_ptr = 0

        for cookie in s:
            if child_ptr < len(g) and cookie >= g[child_ptr]:
                child_ptr += 1

        return child_ptr
