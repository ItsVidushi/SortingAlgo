def count_inversions(arr):
    """
    Count the number of inversions in an array.
    """
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

def read_file_and_count_inversions(filename):
    """
    Read the file and count the number of inversions.
    """
    try:
        with open(filename, 'r') as file:
            data = file.read().split()  # Split by whitespace to get individual integers
            # Convert data to integers
            arr = [int(x) for x in data]
            inversions = count_inversions(arr)
            print("Number of inversions:", inversions)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = "f_s5.txt"
    read_file_and_count_inversions(filename)
