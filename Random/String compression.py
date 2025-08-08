class Solution:
    def compress(self, chars) -> int:
        i=0
        index=0

        while i<len(chars):
            char=chars[i]
            count=0

            while i<len(chars) and chars[i]==char:
                count+=1
                i+=1

            chars[index]=char
            index+=1

            if count>1:
                for digit in str(count):
                    chars[index]=digit
                    index+=1
        return index
        