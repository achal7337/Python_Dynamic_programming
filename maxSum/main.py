# Maximum sum with no adjacent items

def max_sum(arr):

    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)

    ans = [0] * n
    ans[0] = arr[0]
    ans[1] = max(arr[0], arr[1])

    for i in range(2, n):
        ans[i] = max(ans[i-1], ans[i-2]+arr[i])

    return ans[-1]


arr1 = [3, 2, 5, 10, 7]
arr2 = [3, 2, 7, 10]

print(str(max_sum(arr1)) + ',' + str(max_sum(arr2)))
