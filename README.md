# 🚆 Kingdom of Velora Railway System

## 📌 Summary
This project implements several linked list operations for managing a railway cargo system in the Kingdom of Velora.  

We work with:
- **Singly Linked Lists (SLL)** for one-direction cargo tracking  
- **Doubly Linked Lists (DLL)** for two-direction inspection  

The goal is to build, analyze, and repair train cargo structures using efficient algorithms.

---

## 🛠️ Approach

### Task 1: Build Singly Linked List
- Traverse the input Python list
- Create nodes sequentially
- Link each node using `next`
- Maintain order

---

### Task 2: Convert SLL to Python List
- Traverse from `head` to end
- Append each value to a Python list
- Return the result

---

### Task 3: Find First Repeated Value
- Use a `set` to track seen values
- Traverse the list:
  - If value already in set → return it
  - Else add to set
- If no repeats → return `None`

---

### Task 4: Remove All Target Values from DLL
- Traverse the doubly linked list
- For each matching node:
  - Update `prev.next`
  - Update `next.prev`
  - Handle edge cases:
    - Removing head
    - Removing tail
    - Removing all nodes
- Maintain correct `head` and `tail`

---

### Task 5: Palindrome Check (Stretch Task)
- Use two pointers:
  - `left` → head
  - `right` → tail
- Compare values while moving inward
- If mismatch → `False`
- If fully matched → `True`

---

## ⏱️ Complexity

| Task | Time Complexity | Space Complexity |
|------|---------------|-----------------|
| Build SLL | O(n) | O(n) |
| SLL → List | O(n) | O(n) |
| First Repeat | O(n) | O(n) |
| Remove from DLL | O(n) | O(1) |
| Palindrome Check | O(n) | O(1) |

---

## ⚠️ Edge Case Checklist

✔ Empty singly linked list  
✔ Empty doubly linked list  
✔ Single-node lists  
✔ Repeated values  
✔ Removing head node  
✔ Removing tail node  
✔ Removing consecutive nodes  
✔ Removing all nodes  
✔ Palindrome (even length)  
✔ Palindrome (odd length)  

---

## 🧪 Testing

All functions were tested using **pytest**.

Run tests using:
```bash
pytest -q