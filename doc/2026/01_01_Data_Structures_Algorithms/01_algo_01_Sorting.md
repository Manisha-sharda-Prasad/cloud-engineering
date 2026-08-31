# The Sorting Algorithms :
Core mechanics, **Time and Space Complexity**:

## Bubble Sort: ⭐️
- Simplest algorithm, repeatedly **Swapping Adjacent** elements if they are in the wrong order. 
- If not swapped **break** the iteration.
- It has a worst-case complexity of `$O(n^2)$.`

```mermaid
flowchart LR
    subgraph Pass1["Bubble Sort: Adjacent Swaps"]
        direction TB
        S1["[ 5 | 1 | 4 | 2 ]"] -->|"Swap (5 > 1)"| S2["[ 1 | 5 | 4 | 2 ]"]
        S2 -->|"Swap (5 > 4)"| S3["[ 1 | 4 | 5 | 2 ]"]
        S3 -->|"Swap (5 > 2)"| S4["[ 1 | 4 | 2 | (5) ]"]
    end
```
---
## Selection Sort: ⭐️
- **Divides the list** into **sorted and unsorted parts**.
- Picks the **smallest** from **unsorted** side, moves it to **front** of the array.
- Instead of all the shifting, **swap the lowest value**.
- Complexity is `$O(n^2)$.`

```mermaid
flowchart TD
    A["[ 4 | 3 | 1 | 5 ]"] -->|"Find min (1) & Swap with index 0"| B["[(1) | 3 | 4 | 5]"]
    B -->|"Find min in unsorted (3) -> No swap"| C["[(1 | 3) | 4 | 5]"]
    C -->|"Find min in unsorted (4) -> No swap"| D["[(1 | 3 | 4 | 5)] (Sorted)"]
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
    A["[(4) | 3 | 1 | 2]"] -->|"Insert 3 before 4"| B["[(3 | 4) | 1 | 2]"]
    B -->|"Shift (3, 4) right, Insert 1"| C["[(1 | 3 | 4) | 2]"]
    C -->|"Shift (3, 4) right, Insert 2"| D["[(1 | 2 | 3 | 4)]"]
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
    A["[ 4 | 2 | 1 | 3 ]"]
    A -->|"Divide"| B1["[ 4 | 2 ]"]
    A -->|"Divide"| B2["[ 1 | 3 ]"]
    
    B1 --> C1["[ 4 ]"]
    B1 --> C2["[ 2 ]"]
    B2 --> C3["[ 1 ]"]
    B2 --> C4["[ 3 ]"]
    
    C1 & C2 -->|"Merge & Sort"| D1["[ 2 | 4 ]"]
    C3 & C4 -->|"Merge & Sort"| D2["[ 1 | 3 ]"]
    
    D1 & D2 -->|"Merge & Sort"| E["[ 1 | 2 | 3 | 4 ]"]
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
    Root["[ 4 | 2 | 5 | 1 | 3 ]<br>(Pivot: 3)"]
    
    Root --> L1["Left: [ 2 | 1 ]<br>(Pivot: 1)"]
    Root --> Mid1["Pivot: [ 3 ]"]
    Root --> R1["Right: [ 4 | 5 ]<br>(Pivot: 5)"]
    
    L1 --> LL1["[ ]"]
    L1 --> LM1["[ 1 ]"]
    L1 --> LR1["[ 2 ]"]
    
    R1 --> RL1["[ 4 ]"]
    R1 --> RM1["[ 5 ]"]
    R1 --> RR1["[ ]"]

    LL1 & LM1 & LR1 --> JoinedLeft["[ 1 | 2 ]"]
    RL1 & RM1 & RR1 --> JoinedRight["[ 4 | 5 ]"]

    JoinedLeft & Mid1 & JoinedRight --> Result["[ 1 | 2 | 3 | 4 | 5 ]"]
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
flowchart LR
    subgraph Step1["1. Input Array"]
        In["[ 2 | 0 | 2 | 1 | 1 ]"]
    end
    
    subgraph Step2["2. Tally Frequency"]
        direction TB
        F0["Index 0: (1)"]
        F1["Index 1: (2)"]
        F2["Index 2: (2)"]
    end

    subgraph Step3["3. Rebuild Array"]
        Out["[ 0 | 1 | 1 | 2 | 2 ]"]
    end

    In --> Step2 --> Out
```
---

## Radix Sort:⭐️⭐️
- Works with **non-negative integers**.
- Process numbers **digit-by-digit**, data like numbers/specific patterns.
- E.g. if `437` is the highest number in array that needs to be sorted, must sort three times, once for each digit.
- Time complexity depends on the base and the number of digits `($O(d \cdot (n+b))$)`.

```mermaid
flowchart TD
    Input["Input: [ 170 | 045 | 075 | 090 | 002 | 024 ]"]
    
    Input -->|"1. Sort by 1s digit"| D1["[ 170 | 090 | 002 | 024 | 045 | 075 ]"]
    D1 -->|"2. Sort by 10s digit"| D2["[ 002 | 024 | 045 | 170 | 075 | 090 ]"]
    D2 -->|"3. Sort by 100s digit"| D3["[ 002 | 024 | 045 | 075 | 090 | 170 ]"]
    D3 --> Output["Sorted: [ 2 | 24 | 45 | 75 | 90 | 170 ]"]
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