class Solution:
    def balancedString(self, s: str) -> int:
        need = len(s) // 4

        q = max(0, s.count('Q') - need)
        w = max(0, s.count('W') - need)
        e = max(0, s.count('E') - need)
        r = max(0, s.count('R') - need)

        if q == 0 and w == 0 and e == 0 and r == 0:
            return 0

        left = 0
        answer = len(s)

        for right in range(len(s)):

            if s[right] == 'Q':
                q -= 1
            elif s[right] == 'W':
                w -= 1
            elif s[right] == 'E':
                e -= 1
            else:
                r -= 1

            while q <= 0 and w <= 0 and e <= 0 and r <= 0:

                answer = min(answer, right - left + 1)

                if s[left] == 'Q':
                    q += 1
                elif s[left] == 'W':
                    w += 1
                elif s[left] == 'E':
                    e += 1
                else:
                    r += 1

                left += 1

        return answer
