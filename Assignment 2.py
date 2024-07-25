import winsound

# Function to play a beep sound
def beep(frequency, duration):
    winsound.Beep(frequency, duration)

# Function to merge two halves of the array
def merge_sections(array, start, midpoint, end):
    size1 = midpoint - start + 1
    size2 = end - midpoint

    left_half = [0] * size1
    right_half = [0] * size2

    for i in range(size1):
        left_half[i] = array[start + i]

    for j in range(size2):
        right_half[j] = array[midpoint + 1 + j]

    i = 0
    j = 0
    k = start

    while i < size1 and j < size2:
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
        print(f"Merged array: {array}")
        beep(500, 100)  # Beep for each merge step

    while i < size1:
        array[k] = left_half[i]
        i += 1
        k += 1
        print(f"Remaining left half: {array}")
        beep(600, 100)  # Beep for remaining elements in left half

    while j < size2:
        array[k] = right_half[j]
        j += 1
        k += 1
        print(f"Remaining right half: {array}")
        beep(700, 100)  # Beep for remaining elements in right half

# Function to implement merge sort
def sort_and_merge(array, start, end):
    if start < end:
        midpoint = start + (end - start) // 2

        sort_and_merge(array, start, midpoint)
        sort_and_merge(array, midpoint + 1, end)
        merge_sections(array, start, midpoint, end)

# Function to get product IDs from the user
def gather_product_ids():
    input_data = input("Enter product IDs separated by spaces: ")
    product_ids = list(map(int, input_data.split()))
    return product_ids

# Main code to execute the program
if __name__ == "__main__":
    product_ids = gather_product_ids()
    print(f"Original array: {product_ids}")
    sort_and_merge(product_ids, 0, len(product_ids) - 1)
    print(f"Sorted array: {product_ids}")
