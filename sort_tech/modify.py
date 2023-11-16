import time

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
    for i in range(1, len(arr)):
        temp = arr[i]
        location = binary_search(arr, temp, 0, i - 1)
        for j in range(i - 1, location - 1, -1):
            arr[j + 1] = arr[j]
        arr[location] = temp

if __name__ == "__main":
    filename = "l_s5.txt"  # Replace with the actual filename
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            arr = [int(x) for x in data]
            start = time.time()  # Measure the start time here
            binary_insertion_sort(arr)
            end = time.time()  # Measure the end time here
            print("Sorted array:")
            print(" ".join(str(x) for x in arr))
            print("Time taken: ", end - start)  # Calculate and print the time taken
    except FileNotFoundError:
        print("File not found.")
