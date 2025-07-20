# LeetCode Practice: Array & Hashing
Welcome to my LeetCode journey focusing on **Array** and **Hashing**!  
This repository documents learning, solutions, and notes—starting from the absolute basics, moving to advanced concepts, and covering common interview patterns.
---
## Table of Contents 

- [Introduction](#introduction)
- [1. Arrays](#1-arrays)
  - [1.1 What is an Array?](#11-what-is-an-array)
  - [1.2 Basic Operations](#12-basic-operations)
  - [1.3 Array Patterns](#13-array-patterns)
  - [1.4 Example Problems](#14-example-problems)
- [2. Hashing (Hash Table)](#2-hashing-hash-table)
  - [2.1 What is Hashing?](#21-what-is-hashing)
  - [2.2 HashMap & HashSet in Python](#22-hashmap--hashset-in-python)
  - [2.3 Hashing Patterns](#23-hashing-patterns)
  - [2.4 Example Problems](#24-example-problems)
- [3. Advanced Problems](#3-advanced-problems)
- [4. Useful Resources](#4-useful-resources)
- [5. Notes & Tips](#5-notes--tips)

---
## Introduction
Arrays and Hash Tables are **fundamental** data structures in computer science, used everywhere from basic algorithms to high-frequency coding interviews.

### 1.1 What is an Array?
An array is a collection of items stored at contiguous memory locations.

- **Python equivalent:** `list`

#### Example

```pyhton
arr = [1, 2, 3, 4, 5]
print(arr[2]) # Output:3
```

#### 1.2 Basic Operations

| Operation       | Example (Python)    |
| --------------- | ------------------- |
| Access element  | `arr[0]`            |
| Update element  | `arr[2] = 99`       |
| Add at end      | `arr.append(6)`     |
| Insert at index | `arr.insert(1, 10)` |
| Delete by value | `arr.remove(3)`     |
| Delete by index | `del arr[1]`        |
| Length          | `len(arr)`          |
| Slice           | `arr[1:3]`          |


#### 1.3 Arrays Patterns

1. Two Pointers
- Use two indices to traverse/compare elements
- Example: Find if an array has two numbers that sum to target

**Check more examples in [two_pointers](../two_pointers/)**

2. Sliding Window
- Use a window(subarray) to process a range of elements.
- Example: Find maximum sum of k consecutive elements.

**Check more examples in [sliding_window](../sliding_window/)


