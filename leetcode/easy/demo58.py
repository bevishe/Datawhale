import re
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        pattern = '\S*\S'
        res = re.findall(pattern,s)
        return len(res[-1]) if len(res) != 0 else 0

if __name__ == '__main__':
    print(Solution().lengthOfLastWord('he kij  '))