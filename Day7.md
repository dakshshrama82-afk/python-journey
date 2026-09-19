# 📘 Day 7 – File Handling in Python

## 📌 Overview
On Day 7, I explored **Python file handling modes** (`a`, `r+`, `w+`, `a+`) to understand how reading and writing operations behave differently depending on the mode.

---

## 🧩 Problems & Solutions

### 1️⃣ Append Mode (`a`)
**Task:** Open a file in append mode and write data.  
- Appends new content without removing existing data.  
```python
with open("hi.txt", "a") as f:
    data1 = f.write("hi i am thr king")
    print(data1)
