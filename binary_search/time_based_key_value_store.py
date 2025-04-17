class TimeMap(object):

    def __init__(self):
        # key value store
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            # for each key add an array
            self.store[key] = []
        # for each entry add to the array
        self.store[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        result = ""
        # get all values from the array
        values = self.store.get(key, [])
        
        left = 0
        right = len(values) - 1

        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] <= timestamp:
                # lower or equal timestamp
                # move to the left
                result = values[middle][0]
                left = middle + 1
            else:
                # higher move to the right
                right = middle - 1
        
        return result