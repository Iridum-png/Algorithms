def bubble_sort(arr: list) -> list :
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def optimised_bubble_sort(arr: list) -> list :
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr: list) -> list :
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def selection_sort(arr: list) -> list :
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def merge_sort(arr: list) -> list :
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr: list) -> list :
    if len(arr) > 1:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        quick_sort(left)
        quick_sort(right)
        arr[:] = left + [pivot] + right
    return arr

def shell_sort(arr: list) -> list :
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = gap // 2
    return arr

def heap_sort(arr: list) -> list :
    def heapify(arr: list, n: int, i: int) -> None :
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort(arr: list) -> list :
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    sorted_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return sorted_arr

def bucket_sort(arr: list) -> list :
    buckets = [[] for _ in range(10)]
    for i in range(len(arr)):
        buckets[int(arr[i] * 10)].append(arr[i])
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])
    arr[:] = [item for sublist in buckets for item in sublist]
    return arr

def radix_sort(arr: list) -> list :

    max_val = max(arr)
    for i in range(len(str(max_val))):
        buckets = [[] for _ in range(10)]
        for j in range(len(arr)):
            buckets[int(arr[j] % (10 ** (i + 1)) / (10 ** i))].append(arr[j])
        arr[:] = [item for sublist in buckets for item in sublist]
    return arr
