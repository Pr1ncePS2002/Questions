from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter=Counter(magazine)
        for c in ransomNote:
            if counter[c]>0:
                counter[c]-=1
            else:
                return False
        return True
        #     if c not in counter:
        #         return False
        #     elif counter[c]==1:
        #         del counter[c]
        #     else:
        #         counter[c]-=1
        # return True
