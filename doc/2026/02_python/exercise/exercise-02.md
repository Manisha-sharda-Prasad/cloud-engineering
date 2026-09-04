# Python Loops: Hands-On Practice Checklist
```bash
cd /Users/manishaprasad/lekhraj/git/cloud-engineering;
source .venv/bin/activate;
python3 doc/2026/02_python/exercise/exercise-02.py
```

## 8. Solid Square / Rectangle

Given `rows` and `cols`, print a filled grid of stars.

Example:

```text
* * * *
* * * *
* * * *
```

Requirements:

* Use nested loops.
* Outer loop → rows.
* Inner loop → columns.

@[code:section::section-8](exercise-02.py)

---

## 9. Hollow Square / Rectangle

Given `rows` and `cols`, print a grid where stars appear only along the **outer boundaries**.

Example:

```text
* * * *
*     *
*     *
* * * *
```

The inside should remain hollow.

@[code:section::section-9](exercise-02.py)

---

## 10. Left-Aligned Right Triangle

Print a triangle of height `N` where row `i` contains `i` stars.

Example:

```text
*
* *
* * *
* * * *
```
@[code:section::section-10](exercise-02.py)
---

## 11. Inverted Left-Aligned Triangle

Print a triangle that starts with `N` stars and decreases by one star on each subsequent row.

Example:

```text
* * * *
* * *
* *
*
```
@[code:section::section-11](exercise-02.py)
---

## 12. Mirrored (Right-Aligned) Right Triangle

Print a right-angled triangle aligned to the right.

Use leading spaces to position the stars correctly.

Example:

```text
      *
    * *
  * * *
* * * *
```
@[code:section::section-12](exercise-02.py)
---

## 13. Full Equilateral Pyramid

Using leading spaces and an odd-number progression of stars (`2i - 1`), print a centered pyramid of height `N`.

Example:

```text
   *
  ***
 *****
*******
```

@[code:section::section-13](exercise-02.py)

---

## 14. Inverted Full Pyramid

Print an upside-down centered pyramid.

The pattern should start with `2N - 1` stars and decrease to `1` star at the bottom.

Example:

```text
*******
 *****
  ***
   *
```

---

## 15. Diamond Pattern

Combine the logic of the **full pyramid** and **inverted full pyramid** to create a complete diamond.

Example:

```text
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## 16. Hourglass Pattern

Print an inverted pyramid followed by an upright pyramid to create an hourglass shape.

Example:

```text
*******
 *****
  ***
   *
  ***
 *****
*******
```

---

## 17. Hollow Triangle

Print a triangle where only the **outer border** consists of `*`.

The interior should contain spaces.

Example:

```text
*
* *
*   *
*******
```

---

## 18. Number Pyramid

Replace the stars in a left-aligned triangle with the **current row number**.

Example:

```text
1
2 2
3 3 3
4 4 4 4
```

---

## Practice Progression

Work through the problems in this order:

* [ ] 8. Solid Square / Rectangle
* [ ] 9. Hollow Square / Rectangle
* [ ] 10. Left-Aligned Right Triangle
* [ ] 11. Inverted Left-Aligned Triangle
* [ ] 12. Right-Aligned Right Triangle
* [ ] 13. Full Equilateral Pyramid
* [ ] 14. Inverted Full Pyramid
* [ ] 15. Diamond Pattern
* [ ] 16. Hourglass Pattern
* [ ] 17. Hollow Triangle
* [ ] 18. Number Pyramid


---

## Answer sheet
@[code](exercise-02.py)
