import time

def straight_insertion_sort(arr):
    start=time.time()
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    end=time.time()
    diff=end-start
    print("time: ",diff)
    print(arr)


def binary_search(arr, element, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if element == arr[mid]:
            return mid + 1
        elif element > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_insertion_sort(arr):
    start=time.time()
    for i in range(1, len(arr)):
        temp = arr[i]
        location = binary_search(arr, temp, 0, i - 1)
        for j in range(i - 1, location - 1, -1):
            arr[j + 1] = arr[j]
        arr[location] = temp
    end=time.time()
    diff=end-start
    print("time: ",diff)


def shell_sort(arr):
    start=time.time()
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap 
            arr[j] = temp
        gap //= 2
    end=time.time()
    diff=end-start
    print("time: ",diff)


def gnome_sort(arr):
    start=time.time()
    n=len(arr)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    end=time.time()
    diff=end-start
    print("time: ",diff)


MIN_MERGE = 32

def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def tim_sort(arr):
    start_time = time.time()  # Rename the variable 'start' to avoid conflicts
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size
    end_time = time.time()
    diff = end_time - start_time
    print("time:", diff)




if __name__ == "__main__":
    filename = "l_s5.txt"  # Replace with the actual filename
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            arr = [int(x) for x in data]
            print("Binary Insertion Sort")
            binary_insertion_sort(arr)
            print("Straight Insertion Sort")
            straight_insertion_sort(arr)
            print("Shell Sort")
            shell_sort(arr)
            print("Gnome Sort")
            gnome_sort(arr)
            print("Tim Sort")
            tim_sort(arr)

    except FileNotFoundError:
        print("File not found.")
 