from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        sorted_char=sorted(freq.items(),key= lambda x:x[1],reverse=True )
        res=[]
        for char,frequency in sorted_char:
            res.append(char*frequency)
        return ''.join(res)


        
