# The Sorting Algorithms :
Core mechanics, **Time and Space Complexity**:

## Bubble Sort: ⭐️
- Simplest algorithm, repeatedly **Swapping Adjacent** elements if they are in the wrong order. 
- If not swapped **break** the iteration.
- It has a worst-case complexity of `$O(n^2)$.`

```mermaid
flowchart TD

Start([Start Pass]) --> Loop[Compare adjacent arr[j] and arr[j+1]]
Loop --> Cond{arr[j] > arr[j+1]?}
Cond -- Yes --> Swap[Swap arr[j] and arr[j+1]]
Cond -- No --> NoSwap[Keep order]
Swap --> More{More elements in pass?}
NoSwap --> More
More -- Yes --> Loop
More -- No --> CheckSwaps{Any swaps made this pass?}
CheckSwaps -- Yes --> Start
CheckSwaps -- No --> Done([Array is fully sorted])
```

## Selection Sort: ⭐️
- **Divides the list** into **sorted and unsorted parts**.
- Picks the **smallest** from **unsorted** side, moves it to **front** of the array.
- Instead of all the shifting, **swap the lowest value**.
- Complexity is `$O(n^2)$.`

## Insertion Sort: ⭐️
- **One part** of array hold the **sorted values**, **other part** that are **not sorted**.
- sort array one item at a time, **(organizing playing cards, in left-middle-right)**.
- avoids **shift operation**, only when necessary.
- **break** loop, no need to compare when **correct place** for **current value** is found.
- Complexity is `$O(n^2)$.`


---
## Shell Sort:
- An optimized version of insertion sort that uses specific intervals to partially sort data before finalizing.
- Worst-case is `$O(n^2)$.`

## Merge Sort: ⭐️⭐️
- A **divide and conquer** algorithm, first **breaking** it down into **many smaller arrays**,
- then merge **sub-arrays** together the correct way, 
- values from each **sub-array are compared**, so that the **lowest value comes first**.
- Complexity is `$O(n log n)$.`

## Quick Sort: ⭐️⭐️
- Another **divide and conquer** method that uses a **pivot** element to **partition array**.
- 'pivot' moves other so **lower values - Left**, and **higher - Right** of it.
- Implementation: 
  - **quickSort()** calls itself (**Recursion**)
  - **partition()** receives **sub-array**, moves values, **swaps pivot into sub**, 
  - returns **index** where next **split** in **sub-array** happens.
- Average complexity is `$O(n log n)$.`

## Heap Sort: ⭐️⭐️
- Leverages a tree-based "Max Heap" data structure to efficiently sort elements.
- Complexity is `$O(n log n)$.`

## Counting Sort: ⭐️⭐️
- Works on **non-negative integers**(0,1,2,3../ >= 0).
- Sorts integers by counting **number of times** each **value occurs**.
- Implementation:
  - **countingSort()**  receives **array of integers**.
  - Array inside method, **count values**.
  - **loop** inside  method **counts and remove values**, by **incrementing** elements in the **counting array**.
  - Methods used: **max(),enumerate(),extend(),countingSort.**
- Complexity is `$O(n + k)$.`

## Radix Sort:⭐️⭐️
- Works with **non-negative integers**.
- Process numbers **digit-by-digit**, data like numbers/specific patterns.
- E.g. if `437` is the highest number in array that needs to be sorted, must sort three times, once for each digit.
- Time complexity depends on the base and the number of digits `($O(d \cdot (n+b))$)`.

## Tim Sort: 
- A hybrid of insertion and merge sort, notably used in *Python*.
- Complexity is `$O(n log n)$.`

---
## Other Terms:
### Hidden memory shifts: 
- You will not see shifting operations happening in the code if  using high-level programming language such as Python or JavaScript, 
- shifting operations still happening in the background. 
- shifting operations require extra time for the computer to do, which can be a problem.

### Recursion :
- when function **calls itself**, to solve a **smaller piece** of the **same problem**. 
- E.g : Quicksort algorithm,puts pivot element in between sub-array with lower on left and higher on right side, 
- algorithm calls itself twice, so that Quicksort runs again for the sub-array on left and sub-array right.
- algorithm call itself until sub-arrays are too small to be sorted.