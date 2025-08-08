class Solution:
    def findRestaurant(self, list1, list2):
        new_dict={}
        for i in range(len(list1)):
            word=list1[i]
            new_dict[word]=i
        min_sum=float('inf')
        result=[]
        for j in range(len(list2)):
            word=list2[j]
            if word in new_dict:
                total=j+new_dict[word]
                if total<min_sum:
                    result=[word]
                    min_sum=total
                elif total==min_sum:
                    result.append(word)
        return result        

        