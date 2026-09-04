# Run with this: python3 src/DSA/Algorithm/bubbleSort.py
data = [60, 64, 34, 25, 12, 22, 11]

# Looping with Conditions (if)
# Main Bubble-Sort Program : (Connecting Nested Loops to Bubble Sort - O(N^))
def bubble_sort(arr):                 # make a function
    n = len(arr)

    for i in range(0,n):
        print(f"Starting Pass {i+1}--")

        for j in range(0, (n-1)-i):
            print(f"Checking Pair: ({arr[j]}, {arr[j+1]})")

            if arr[j] > arr[j+1]:                    # if > swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Main swapping program
                print(f" --> Swapped! New Array: {arr}")

    return arr

# === Main ===
if __name__ == '__main__':
    bubble_sort(data)         # calling the function

