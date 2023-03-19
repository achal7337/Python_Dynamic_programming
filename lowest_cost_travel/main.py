# We want to go from city 0 to city n using busesWe want to go from city 0 to city n using buses
# The cost of going from i to j is C(ij) > 0, for all (i, j) satisfying i < j
# All buses only go from a lower-numbered city to a higher-numbered city
# What is the minimum cost of going from 0 to n?
import math


def lowest_cost(arr):
    ans = len(arr)
    ans[0] = 0
    cost = [0] * ans
    for i in range(1, len(arr)):
        cost[i] = arr[0][i]

    return ans[len(arr)]


arr1 = [3, 5, 4]
arr2 = [3, 2, 7, 10]

print(lowest_cost(arr1))
