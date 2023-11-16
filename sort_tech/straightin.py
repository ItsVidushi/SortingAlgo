def straight_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def read_file_and_sort(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()  # Split by whitespace to get individual integers
            arr = [int(x) for x in data]  # Convert data to integers
            straight_insertion_sort(arr)
            print("Sorted array:", arr)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = "1000_f_s3.txt"  # Replace with the actual file name containing data
    read_file_and_sort(filename)
