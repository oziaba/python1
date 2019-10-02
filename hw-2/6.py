#6
def get_two_sum(nums, k):
    c = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                c +=1
                return [i, j]
    if c == 0:
        return 'None'
get_two_sum([2, 17, 7, 5], 9)