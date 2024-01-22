#i made this
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        ran = False
        while i < len(s) - 1:
            if values[s[i+1]] > values[s[i]]:
                num += values[s[i+1]] - values[s[i]]
                if s[i+1] == s[-1]:
                    skip = True
                else:
                    skip = False
                i+=2
            else:
                num += values[s[i]]
                i +=1
                skip = False
            ran = True
        if ran:
            if not skip:
                num += values[s[i]]
        if not ran:
            num += values[s[i]]
        return num