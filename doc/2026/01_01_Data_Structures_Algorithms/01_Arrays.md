
# The Sorting Algorithms :
10 popular sorting algorithms,core mechanics, time and space complexity:

### Bubble Sort:
- The simplest algorithm, repeatedly swapping adjacent elements if they are in the wrong order. 
- If not swapped -**break**.It has a worst-case complexity of $O(n^2)$.
### Selection Sort: 
- Divides the list into sorted and unsorted parts, repeatedly picking the smallest element from the unsorted side. 
- Complexity is $O(n^2)$.
### Insertion Sort: 
- Builds a sorted array one item at a time, similar to organizing a hand of playing cards. 
- Complexity is $O(n^2)$.
### Merge Sort: 
- A "divide and conquer" algorithm that splits the list into single units before merging them back in order. 
- Complexity is $O(n \log n)$.
### Quick Sort: 
- Another divide and conquer method that uses a "pivot" element to partition data.
- Average complexity is $O(n \log n)$.
### Heap Sort:
- Leverages a tree-based "Max Heap" data structure to efficiently sort elements.
- Complexity is $O(n \log n)$.
### Counting Sort:
- Sorts integers by counting the frequency of each value within a specific range.
- Complexity is $O(n + k)$.
### Shell Sort:
- An optimized version of insertion sort that uses specific intervals to partially sort data before finalizing.
- Worst-case is $O(n^2)$.
### Tim Sort:
- A hybrid of insertion and merge sort, notably used in *Python*.
- Complexity is $O(n \log n)$.
### Radix Sort: 
- Processes numbers digit-by-digit, often used for data like numbers or specific patterns. 
- Time complexity depends on the base and the number of digits ($O(d \cdot (n+b))$).