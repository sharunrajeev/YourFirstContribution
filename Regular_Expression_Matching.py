from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == - 1:
                return i == -1

            if p[j] == '*':
                if dp(i, j - 2):
                    return True  # s = ba, p = bab*
                if i >= 0 and (s[i] == p[j - 1] or p[j - 1] == '.') and dp(i - 1, j):
                    return True  # s = ba, p = ba* or b.*
            if i >= 0 and (s[i] == p[j] or p[j] == '.') and dp(i - 1, j - 1):
                return True  # s = bac, p = bac or ba.
            
            return False

        s, p = map(list, (s, p))
        m, n = map(len, (s, p))
        return dp(m - 1, n - 1)
