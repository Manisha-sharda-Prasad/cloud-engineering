# The Sorting Algorithms :
Core mechanics, **Time and Space Complexity**:

## Bubble Sort: ⭐️
- Simplest algorithm, repeatedly **Swapping Adjacent** elements if they are in the wrong order. 
- If not swapped **break**.
- It has a worst-case complexity of `$O(n^2)$.`

## Selection Sort: ⭐️
- **Divides the list** into **sorted and unsorted parts**.
- Picks the **smallest** element from **unsorted** side, moves it to **front** of the array.
- Instead of all the shifting, **swap the lowest value**.
- Complexity is `$O(n^2)$.`

## Insertion Sort: ⭐️
- **One part** of array hold the **sorted values**, **other part** that are **not sorted yet**.
- sorted array one item at a time, **(organizing playing cards)**. 
- avoids most of the **shift operation**, only shifting the values necessary.
- **break** loop,no need to compare when **correct place** for **current value** is found.
- Complexity is `$O(n^2)$.`

## Shell Sort:
- An optimized version of insertion sort that uses specific intervals to partially sort data before finalizing.
- Worst-case is `$O(n^2)$.`

---
## Merge Sort: ⭐️⭐️
- A "divide and conquer" algorithm that splits the list into single units before merging them back in order. 
- Complexity is `$O(n \log n)$.`

## Quick Sort: ⭐️⭐️
- Another **divide and conquer** method that uses a **pivot** element to **partition array**.
- 'pivot' moves other so **lower values - Left**, and **higher - Right** of it.
- Implementation: 
  - **'quickSort' method** calls itself (**Recursion**)
  - **'partition' method** receives **sub-array**, moves values, **swaps pivot into sub**, **returns index** where **next split** in **sub-array** happens.
- Average complexity is `$O(n \log n)$.`

## Heap Sort: ⭐️⭐️
- Leverages a tree-based "Max Heap" data structure to efficiently sort elements.
- Complexity is `$O(n \log n)$.`

## Counting Sort: ⭐️⭐️
- Works on **non negative integers**(0,1,2,3../ >= 0).
- Sorts integers by **counting** the **number of times** each **value occurs**.
- Implementation:
  - **'countingSort' method**  receives **array of integers**.
  - Array inside method, **count values**.
  - **loop** inside  method, **counts - removes values**, by **incrementing** elements in the **counting array**.
  - Methods used: **max(),enumerate(),extend(),countingSort.**
- Complexity is `$O(n + k)$.`

## Tim Sort: 
- A hybrid of insertion and merge sort, notably used in *Python*.
- Complexity is `$O(n \log n)$.`

## Radix Sort: 
- Processes numbers digit-by-digit, often used for data like numbers or specific patterns. 
- Time complexity depends on the base and the number of digits ($O(d \cdot (n+b))$).

---
## Other Terms:
### Hidden memory shifts: 
- You will not see shifting operations happening in the code if  using high-level programming language such as Python or JavaScript, 
- shifting operations still happening in the background. 
- shifting operations require extra time for the computer to do, which can be a problem.

### Recursion :
- is when a function calls itself, to solve a smaller piece of the same problem. 
- E.g : Quicksort algorithm,puts pivot element in between sub-array with lower on left and higher on right side, 
- algorithm calls itself twice, so that Quicksort runs again for the sub-array on left and sub-array right.
- algorithm call itself until sub-arrays are too small to be sorted.