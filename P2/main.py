# simple fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci with memoization
def memo(n, arr=None):
    if arr is None:
        arr = {}
    if n in arr:
        return arr[n]
    if n <= 1:
        return n
    result = memo(n - 1, arr) + memo(n - 2, arr)
    arr[n] = result
    return result


# fibonacci with tabulation
def tabulation(n):
    if n <= 1:
        return n
    tab = [0] * (n + 1)
    tab[0] = 0
    tab[1] = 1
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]


print(str(fibonacci(10)) + ',' + str(tabulation(10))+',' + str(memo(10)))
