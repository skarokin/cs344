def max_contig_subseq(nums):
    '''
    ALGORITHM:
        initialize dp array with 0s
        dp[0] = nums[0] (obviously)
        initialize start and end of list slice to 0
        for each element in nums:
            if adding nums[i] to previous sum is greater than nums[i] itself:
                we can extend the subsequence
            else, we need to start a new subsequence
            if a new largest sum is found:
                update the end index
    '''
    n = len(nums)
    dp = [0] * n 
    dp[0] = nums[0]
    start = end = 0

    for i in range(1, n):
        if dp[i-1] + nums[i] > nums[i]:
            dp[i] = dp[i-1] + nums[i]
            end=i
        else:
            dp[i] = nums[i]
            start = i

        if dp[i] > dp[end]:
            end = i

    return (start, end, dp[end])

arr = [5, 15, -30, 10, -5, 40, 10]

print(max_contig_subseq(arr))