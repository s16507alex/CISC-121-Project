---
title: CISC121 Project
emoji: 📊
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
---

# Linear Search Algorithm Simulator

## Demo Video
https://cdn-uploads.huggingface.co/production/uploads/6928cb029054d07947ebffc6/P-U8MuN7ccZIeVeBoIvpE.qt

## Example Test Cases

### **Test 1 — Target Found, Correct Guess**
- List: `[4, 9, 12, 18, 23, 27, 31, 35, 40, 44, 49]`
- Target: `31`
- Guess: `6`
- Expected:  
  - Algorithm finds 31 at index 6
  - Gamification: guess matches found index  
  - Score increments  
  - Correct-guess message appears  
- Result: ✔ *Passed*

### **Test 2 — Target Found, Wrong Guess**
- List: `[3, 8, 11, 17, 22, 26, 30, 33, 38, 41, 47]`
- Target: `22`
- Guess: `0`
- Expected:  
  - Algorithm finds 22 at index 4
  - Guess is wrong
  - Score does **not** increment  
  - “Incorrect Guess” message appears  
- Result: ✔ *Passed*

### **Test 3 — Target Not Found**
- List: `[1, 6, 10, 15, 19, 24, 29, 34, 39, 45, 50]`
- Target: `999`
- Guess: `5`
- Expected:  
  - Algorithm reports “not found”  
  - Gamification message says guessing doesn't apply  
  - Score unchanged  
- Result: ✔ *Passed*

### **Test 4 — Invalid Input**
- Target entered: `"abc"`
- Expected:
  - Error message  
  - No crash  
- Result: ✔ *Passed*

### **Test 5 — User clicked “Run” without generating list**
- Expected:  
  - Warning message “Generate List first”  
  - No steps shown  
  - No crash  
- Result: ✔ *Passed*

### **Test 6 — Score Persistence Test**
- Ran multiple searches with different guesses  
- Expected:  
  - Score persists across runs  
  - Score increments only on correct guesses  
- Result: ✔ *Passed*


## Problem Breakdown & Computational Thinking

### Flowchart of the Algorithm


---

### Computational Thinking (4 Pillars)

#### **1. Decomposition**
The problem is broken into smaller functional parts:

Input module
- generate_list(): produces a random list for deterministic testing.
- UI inputs (target, guess): validation responsibility (type/range).

Core algorithm module
- linear_search_on_state(): iterates through the list, generates textual step traces, and produces snapshots for remaining in the list.

Gamification module
- Guess evaluation and a persistent score_state: handles score changes and user feedback (win/lose).

UI module
- Gradio Blocks wiring: maps outputs to textboxes, handles state persistence.

Testing / Logging module
- Example test cases, and explicit messages for invalid or missing inputs.

#### **2. Pattern Recognition**
- Each loop iteration performs the same three actions: read arr[i], compare it to target, append a step message. This repetition is the basis of linear search and suggests that a simple for loop is the correct structure.
- After each check, the “remaining list” is arr[i+1:], this transforms the global list perception into a sliding window that always advances by 1. Recognizing this pattern gives a single expression for the remaining list rather than increasing manually.
- If arr[i] == target, the loop terminates early. Pattern recognition shows many inputs will be found early in best-case, so early exit preserves efficiency.
- The guess-checking pattern is a simple equality check guess == found_index and only interacts with score on the single success pattern. This isolates side effects to one clear condition.

These patterns justify the chosen control flow and the decision to keep gamification logic separate from the core loop. 

#### **3. Abstraction**
Users only see:
- List  
- Steps  
- Remaining list  
- Result  
- Score  

Users do **not** see:
- loops  
- variables  
- index handles  
- internal state  
- Python code  

Abstraction makes the algorithm easier to understand for beginners.

#### **4. Algorithm Design**
Pseudocode:
function linear_search(arr, target):
    for i from 0 to len(arr)-1:
        emit "Check index i: value arr[i]"
        emit "Remaining elements -> arr[i+1:]"
        if arr[i] == target:
            emit "Found at index i"
            return found_index = i
    emit "Not found"
    return found_index = None

Loop invariant: Before each iteration i, all elements at indices 0..i-1 have been checked and are not equal to target.

Initialization: before i=0, zero elements checked, invariant holds meaninglessly.

Maintenance: at iteration i, check arr[i]; if it equals the target we return (correct), otherwise the invariant holds for the next iteration i+1 because arr[i] has been proven not equal.

Termination: if loop ends with no returns, all indices 0..n-1 have been checked and none matched, conclude that target is not present.

Time complexity
Best case: O(1), target at index 0, return immediately.
Average/Worst case: O(n), target near middle or absent (must check all elements).

Space complexity
O(n) for the output trace (store step messages and remaining-list snapshots). In-place search would be O(1), but for pedagogical trace, accept O(n) extra output.

---

## Steps to Run

### **1. Install dependencies**
pip install -r requirements.txt

### **2. Run the app**
python app.py

### **3. Open the Gradio link in browser**  
The app will launch automatically and show a URL

---

## Hugging Face Link
https://huggingface.co/spaces/s16507alex/CISC121-Project

---

## Author & Acknowledgment
Created by **Alex Liang** for the **CISC-121 Python Project**.  
