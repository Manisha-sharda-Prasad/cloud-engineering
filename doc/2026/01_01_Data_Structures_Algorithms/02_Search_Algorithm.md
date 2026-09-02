## Linear Search :
- checks each item in a collection **one by one** until the target is found.
- It has an `O(n)` Complexity, the number of operations grows directly with the number of items.
- Ideal for **Unsorted Lists/ Small collections** where checking every item is feasible.

```mermaid
flowchart TD
    Start["Target = 7"] --> Step1
    Step1["[ (2) | 4 | 7 | 9 ] : 2 == 7 ? No"] --> Step2
    Step2["[ 2 | (4) | 7 | 9 ] : 4 == 7 ? No"] --> Step3
    Step3["[ 2 | 4 | (7) | 9 ] : 7 == 7 ? Match found at Index 2!"]
```

--- 

## Binary Search:
- **"Divide and Conquer"** approach, starts in the **middle of sorted list**, 
- then repeatedly **Eliminates half** of the remaining search space - **Target is Higher - Lower**.
- Extremely **fast**; e.g. finds an item in 1,000,000 entries in only about 20 steps.
- only works on **sorted data**, e.g. **Contacts - Phone Number**

```mermaid
flowchart TD
    Target["Target = 11"] --> S1
    
    subgraph Step1["Step 1"]
        S1["[ 1 | 3 | 5 | (7) | 9 | 11 | 13 ]<br>Mid = 7 (7 < 11 -> Search Right)"]
    end
    
    subgraph Step2["Step 2"]
        S2["[ 9 | (11) | 13 ]<br>Mid = 11 (11 == 11 -> Found at Index 5!)"]
    end
    
    S1 --> S2
```