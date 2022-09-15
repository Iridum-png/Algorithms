def linear_search(arr: list, target) -> int :
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr: list, target) -> int :
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def jump_search(arr: list, target) -> int :
    from math import sqrt
    n = len(arr)
    step = int(sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

def interpolation_search(arr: list, target) -> int :
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr: list, target) -> int :
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        mid = low + int(2 ** (high - low) * (target - arr[low]) / (arr[high] - arr[low]))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def sublist_search(arr: list, sublist) -> int :
    n = len(arr)
    m = len(sublist)
    for i in range(n - m + 1):
        if arr[i:i + m] == sublist:
            return i
    return -1

def fibbonacci_search(arr: list, target) -> int :
    def fib(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return a
    n = len(arr)
    f = fib(n)
    while f < n:
        i = f - (fib(f) - 1)
        if arr[i] == target:
            return i
        elif arr[i] < target:
            f += 1
        else:
            f -= 1
    return -1
