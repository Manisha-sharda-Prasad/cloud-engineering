
# run with this: python3 src/DSA/Algorithm/bubbleSort.py

data = [60, 64, 34, 25, 12, 22, 11]
# Looping with Conditions (if)
for d in data:
    if d >= 34:
        print(f"Greater or Equal to '34':{d}")   # 64 34 90

# Looping Even Numbers
for d in data:
    if d % 2 == 0:
        print(d)

# Looping with range()
for num in range(7,14):
    print(f"Count: {num}")


# Compare Every Pair - prints possible adjacent comparison in a short list
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        print(f"Comparing {data[i]} with {data[j]}")





# Connecting Nested Loops to Bubble Sort - O(N^)
def bubble_sort(arr):    #make a function
    n = len(arr)

    for i in range(0,n):
        print(f"Starting Pass {i+1}--")

        for j in range(0, (n-1)-i):
            print(f"Checking Pair: ({arr[j]}, {arr[j+1]})")

            if arr[j] > arr[j+1]:     #if > swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f" --> Swapped! New Array: {arr}")

    return arr
bubble_sort(data)         #calling the function