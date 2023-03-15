def sum1(num, i):
    if i >= len(num):
        return 0
    return max(num[i] + sum1(num, i + 2), sum1(num, i + 1))


def maxsum(arr, n):
    return sum1(arr, 0)


if __name__ == "__main__":
    # Creating the array
    arr = [5, 5, 10, 100, 10, 5]
    N = len(arr)

    # Function call
    print(maxsum(arr, N))
