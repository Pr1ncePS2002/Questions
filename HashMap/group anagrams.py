class Solution:
    def groupAnagrams(self, strs) :
        new_dict={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word in new_dict:
                new_dict[sorted_word].append(word)
            else:
                new_dict[sorted_word]=[word]
        return list(new_dict.values())
        
        