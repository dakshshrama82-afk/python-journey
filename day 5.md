# Day 5: Word & Text Analyzer

A menu-driven, console-based program that collects multiple sentences from the user and analyzes them using everything learned so far — input/lists, if/elif/else, dictionaries, sets, and loops.

## Requirements

### 1. Collect Input
- Keep asking the user to enter a sentence.
- Stop collecting when the user types `done`.
- Store every sentence entered in a **list**.

### 2. Process the Text
- Convert all text to lowercase (so `"The"` and `"the"` are treated as the same word).
- Split each sentence into individual words.
- Strip punctuation from words (e.g. `"cat,"` should become `"cat"`).

### 3. Word Frequency Count (Dictionary)
- Build a dictionary that maps each word to how many times it appeared across **all** sentences combined.

### 4. Unique Words (Set)
- Find the set of all distinct words used across every sentence.

### 5. Common Words (Set Intersection)
- Find the words that appear in **every single sentence** entered (not just somewhere overall).

### 6. Word Length Categorization (if / elif / else)
- Classify every unique word into one of three buckets:
  - **Short**: fewer than 4 letters
  - **Medium**: 4–6 letters
  - **Long**: 7 or more letters
- Count how many words fall into each bucket.

### 7. Final Report
Print a summary report showing:
- Total number of words entered (including repeats)
- Total number of unique words
- The most frequently used word, and how many times it appeared
- The list of words common to every sentence
- Count of short / medium / long words

## Example

**Input:**
```
Enter a sentence (or 'done' to stop): The cat sat on the mat
Enter a sentence (or 'done' to stop): The dog sat near the cat
Enter a sentence (or 'done' to stop): done
```

**Expected-style Output:**
```
Total words entered: 12
Unique words: 7
Most frequent word: "the" (4 times)
Words common to every sentence: the, cat, sat
Short words: 5 | Medium words: 2 | Long words: 0
```

## Constraints / Notes
- Use only what you've learned so far: `input`, `print`, type conversion, lists, if/elif/else, dictionaries, sets, while loops, for loops.
- Do not use any built-in word-counting libraries (e.g. `collections.Counter`) — write the counting logic yourself.
- Handle punctuation (`.`, `,`, `!`, `?`) so it doesn't break word matching.
