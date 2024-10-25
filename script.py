class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True # strings already equal.
        newstr = []
        for i, c in enumerate(s1):
            if s2[i] != c:
                newstr.append(i)

        if len(newstr) == 2:
            i, j = newstr[0], newstr[1]
            a  = list(s1)
            a[i] = s1[j]
            a[j] = s1[i]

            return ''.join(a) == s2
        return False
