# 04 File Organization & Indexing

## 1. File Organization

- **Heap File:** Records are placed anywhere in the file (unordered). Fast insertion, slow search.
- **Sequential File:** Records are sorted by a search key. Fast binary search, expensive insertion.
- **Hash File:** Record location is determined by a hash function on the search key.

## 2. Indexing

An auxiliary data structure to speed up data retrieval.

Indexes speed up `SELECT` but slow down `INSERT`, `UPDATE`, and `DELETE` due to maintenance overhead.

**1. By Physical Storage**

- **Clustered Index:** Defines the physical order of data in the table. Only one per table.
- **Non-Clustered Index:** A separate structure from data rows; contains pointers to the actual data.

**2. By Entry Density**

- **Dense Index:** An index record appears for every search-key value in the file. Faster search, more space.
- **Sparse Index:** Records created for only some values. Uses less space; requires sorted data.

**3. By Column Role**

- **Primary Index:** Built on the ordering key (usually the PK). Often automatically clustered.
- **Secondary Index:** Built on non-ordering attributes. Usually non-clustered and dense.

## 3. B and B+ Trees

Most modern databases don't just store indexes as flat lists; they use tree structures to keep search times logarithmic $O(\log n)$.

Balanced search trees optimized for disk storage (minimizing I/O).

| Feature          | B-Tree                                                   | B+ Tree                                                          |
| :--------------- | :------------------------------------------------------- | :--------------------------------------------------------------- |
| **Data Storage** | Data pointers stored in **Internal** and **Leaf** nodes. | Data pointers stored **only** in **Leaf** nodes.                 |
| **Leaf Linking** | Leaves are not linked.                                   | Leaves are linked (Linked List) for efficient sequential access. |
| **Height**       | Higher (keys + data take space in internal nodes).       | Lower (internal nodes only hold keys, high fan-out).             |
| **Search**       | Can end at internal node.                                | Must always traverse to leaf.                                    |
| **Range Query**  | Slow (requires tree traversal).                          | Very Fast (follow leaf links).                                   |
