class Solution:
    def getLastMoment(self, n, left, right):
        lastMoment = 0

        for pos in left:
            lastMoment = max(lastMoment, pos)

        for pos in right:
            lastMoment = max(lastMoment, n - pos)

        return lastMoment