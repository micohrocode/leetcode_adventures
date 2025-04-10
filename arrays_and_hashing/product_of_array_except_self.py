def productExceptSelf(self, nums):
        n = len(nums)
        # storage of the answers
        res = [1] * n

        prefix = 1
        # the first has no prefex so = 1
        # then everything after that is multiplied
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        # start at the end, the end has no postfix so *= 1
        # then everything after that is multiplied by what is after it
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res