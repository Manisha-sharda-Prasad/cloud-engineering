# The Sorting Algorithms :
Core mechanics, **Time and Space Complexity**:

## Bubble Sort: ⭐️
- Simplest algorithm, repeatedly **Swapping Adjacent** elements if they are in the wrong order. 
- If not swapped **break** the iteration.
- It has a worst-case complexity of `$O(n^2)$.`

```mermaid
flowchart TD

Start([Start Pass]) --> Loop["Compare adjacent arr[j] and arr[j+1]"]
Loop --> Cond{"arr[j] > arr[j+1]?"}
Cond -- Yes --> Swap["Swap arr[j] and arr[j+1]"]
Cond -- No --> NoSwap[Keep order]
Swap --> More{More elements in pass?}
NoSwap --> More
More -- Yes --> Loop
More -- No --> CheckSwaps{Any swaps made this pass?}
CheckSwaps -- Yes --> Start
CheckSwaps -- No --> Done(["Array is fully sorted"])
```
---
## Selection Sort: ⭐️
- **Divides the list** into **sorted and unsorted parts**.
- Picks the **smallest** from **unsorted** side, moves it to **front** of the array.
- Instead of all the shifting, **swap the lowest value**.
- Complexity is `$O(n^2)$.`

```mermaid
  flowchart TD
  Start([Set i = 0 to n - 1]) --> FindMin["Scan unsorted part arr[i...n-1] to find min_index"]
  FindMin --> Check{min_index != i?}
  Check -- Yes --> Swap["Swap arr[i] with arr[min_index]"]
  Check -- No --> Next[i = i + 1]
  Swap --> Next
  Next --> DoneCheck{i < n - 1?}
  DoneCheck -- Yes --> FindMin
  DoneCheck -- No --> Done(["Array is fully sorted"])
```
---

## Insertion Sort: ⭐️
- **One part** of array hold the **sorted values**, **other part** that are **not sorted**.
- sort array one item at a time, **(organizing playing cards, in left-middle-right)**.
- avoids **shift operation**, only when necessary.
- **break** loop, no need to compare when **correct place** for **current value** is found.
- Complexity is `$O(n^2)$.`

```mermaid
flowchart TD
%% Define standard node shapes for clarity
  StartNode(["Start Pass: key = arr[i], j = i-1"])
DecideBoundary{j >= 0?}
DecideValue{"arr[j] > key?"}
ActionShift["Shift arr[j] to arr[j+1]"]
ActionDec[j = j - 1]
ActionInsert["Insert key at arr[j+1]"]
DecideMore{More elements i?}
ActionNextI[i = i + 1]
EndNode([Done: Array Sorted])

%% Define corrected logical flow
StartNode --> DecideBoundary

%% The inner comparison loop
DecideBoundary -- Yes --> DecideValue
DecideValue -- Yes --> ActionShift
ActionShift --> ActionDec
ActionDec --> DecideBoundary

%% Exit paths from the inner loop (both go to Insert)
DecideBoundary -- No --> ActionInsert
DecideValue -- No --> ActionInsert

%% The outer loop
ActionInsert --> DecideMore
DecideMore -- Yes --> ActionNextI
ActionNextI --> StartNode
DecideMore -- No --> EndNode
```
---

## Shell Sort:
- An optimized version of insertion sort that uses specific intervals to partially sort data before finalizing.
- Worst-case is `$O(n^2)$.`
---

## Merge Sort: ⭐️⭐️
- A **divide and conquer** algorithm, first **breaking** it down into **many smaller arrays**,
- then merge **sub-arrays** together the correct way, 
- values from each **sub-array are compared**, so that the **lowest value comes first**.
- Complexity is `$O(n log n)$.`

```mermaid
flowchart TD
    Start([merge_sort arr]) --> Base{len arr <= 1?}
    Base -- Yes --> ReturnArr([Return arr])
    Base -- No --> Split[Split into Left and Right halves]
    Split --> RecurseLeft[merge_sort Left]
    Split --> RecurseRight[merge_sort Right]
    RecurseLeft --> Merge[Merge sorted Left and Right into one array]
    RecurseRight --> Merge
    Merge --> ReturnMerged([Return Merged Array])
```    
---

## Quick Sort: ⭐️⭐️
- Another **divide and conquer** method that uses a **pivot** element to **partition array**.
- 'pivot' moves other so **lower values - Left**, and **higher - Right** of it.
- Implementation: 
  - **quickSort()** calls itself (**Recursion**)
  - **partition()** receives **sub-array**, moves values, **swaps pivot into sub**, 
  - returns **index** where next **split** in **sub-array** happens.
- Average complexity is `$O(n log n)$.`

```mermaid
flowchart TD
Start([quick_sort arr]) --> Base{len arr <= 1?}
Base -- Yes --> ReturnArr([Return arr])
Base -- No --> Pivot[Choose Pivot element]
Pivot --> Partition[Partition array into:<br/>Left: < Pivot<br/>Mid: == Pivot<br/>Right: > Pivot]
Partition --> RecurseLeft[quick_sort Left]
Partition --> RecurseRight[quick_sort Right]
RecurseLeft --> Concat[Combine Left + Mid + Right]
RecurseRight --> Concat
Concat --> ReturnSorted([Return Sorted Array])
```

---
## Heap Sort: ⭐️⭐️
- Leverages a tree-based "Max Heap" data structure to efficiently sort elements.
- Complexity is `$O(n log n)$.`

---
## Counting Sort: ⭐️⭐️
- Works on **non-negative integers**(0,1,2,3../ >= 0).
- Sorts integers by counting **number of times** each **value occurs**.
- Implementation:
  - **countingSort()**  receives **array of integers**.
  - Array inside method, **count values**.
  - **loop** inside  method **counts and remove values**, by **incrementing** elements in the **counting array**.
  - Methods used: **max(),enumerate(),extend(),countingSort.**
- Complexity is `$O(n + k)$.`
```mermaid
flowchart TD
    Start([Input Array & Find Max Value K]) --> Init[Initialize Count array of size K + 1 with 0s]
    Init --> Freq["Iterate input array: increment Count[x]"]
    Freq --> Reconstruct[Iterate Count array from 0 to K]
    Reconstruct --> Append[Append each value x freq times into Output Array]
    Append --> Done([Return Output Array])
```
---

## Radix Sort:⭐️⭐️
- Works with **non-negative integers**.
- Process numbers **digit-by-digit**, data like numbers/specific patterns.
- E.g. if `437` is the highest number in array that needs to be sorted, must sort three times, once for each digit.
- Time complexity depends on the base and the number of digits `($O(d \cdot (n+b))$)`.

```mermaid
flowchart TD
    Start([Find maximum number to get total digits d]) --> SetExp[Set exp = 1 least significant digit]
    SetExp --> Loop{max_val / exp > 0?}
    Loop -- No --> Done([Array is fully sorted])
    Loop -- Yes --> Distribute[Distribute elements into 0-9 buckets using current digit]
    Distribute --> Collect[Flatten buckets back into array]
    Collect --> NextDigit[exp = exp * 10]
    NextDigit --> Loop
```

---
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