class Solution(object):
    def canConstruct(self,ransomNote, magazine):
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        dit = {}
        for i in range(len(magazine)):
            if magazine[i] in dit:
                dit[magazine[i]] += 1
            else:
                dit[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in dit:
                return False
            elif dit[ransomNote[i]] == 0:
                return False
            else:
                dit[ransomNote[i]] -= 1
        return True

