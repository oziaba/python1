#7
def get_three_sum(nums, k):
    c = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for x in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[x] == k:
                    c +=1
                    return [i, j, x]
    if c == 0:
        return 'None'
get_three_sum([2, 7, 11, 15], 24)