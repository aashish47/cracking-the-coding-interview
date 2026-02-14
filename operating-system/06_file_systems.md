# 06 File Systems

## 1. File Concept

- **File:** A named collection of related information recorded on secondary storage.
- **Attributes:** Name, Identifier, Type, Location, Size, Protection, Time/Date.
- **Operations:** Create, Write, Read, Reposition (Seek), Delete, Truncate.

## 2. Directory Structure

- **Single-Level:** All files in one directory. Naming collisions.
- **Two-Level:** User File Directory (UFD) per user.
- **Tree-Structured:** Standard hierarchy (Folders/Sub-folders).
- **Acyclic Graph:** Allows sharing (Aliases/Shortcuts/Links).

## 3. Allocation Methods

How disk blocks are assigned to files.

### 3.1 Contiguous Allocation

- File occupies a set of contiguous blocks.
- **Pros:** Excellent read performance (minimized seek time). Simple.
- **Cons:** External fragmentation. Hard to extend file size.

### 3.2 Linked Allocation

- Each file is a linked list of blocks. Directory points to first and last.
- **Pros:** No external fragmentation. Easy to grow.
- **Cons:** Slow random access (must traverse list). Pointers consume space. Reliability (lost pointer = lost file).

### 3.3 Indexed Allocation (e.g., Unix Inode)

- Brings all pointers together into one block: the **Index Block**.
- **Pros:** Supports direct access. No external fragmentation.
- **Cons:** Wasted space for small files (overhead of index block).

| Method         | Sequential Access | Random Access | Fragmentation       |
| :------------- | :---------------- | :------------ | :------------------ |
| **Contiguous** | Fast              | Fast          | External            |
| **Linked**     | Good              | Poor          | Internal (pointers) |
| **Indexed**    | Good              | Good          | None                |

## 4. Free Space Management

Tracking available disk blocks.

1.  **Bit Vector (Bitmap):**
    - 1 bit per block (1 = Free, 0 = Occupied).
    - _Fast_ to find first free block. _Space efficient_ if disk is small.
2.  **Linked List:**
    - Free blocks are linked together.
    - _No space overhead_ (stored in free blocks themselves). _Slow_ traversal.
3.  **Grouping/Counting:** Variations of linked list to store multiple free block addresses in one block.
