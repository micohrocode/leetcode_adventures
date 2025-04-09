def topKFrequent(self, nums, k):
    res = {}

    for i,v in enumerate(nums):
        # track how many times each letter appears
        if v in res.keys():
            res[v] += 1
        else:
            res[v] = 1
                
    # format the answer
    answer = res.items()
    answer.sort(key=lambda x: x[1])
        
    # return only the amount it asks for: k
    return [x[0] for x in answer][-k:]