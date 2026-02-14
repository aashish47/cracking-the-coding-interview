# 02 Relational Model

Represents data as a collection of relations (tables).

- **Relation:** Table.
- **Tuple:** Row (Record).
- **Attribute:** Column (Field).
- **Schema:** The logical structure (e.g., `Student(ID, Name, Age)`).

### Database vs. Schema vs. Relation

| Term         | Scope       | Description                                           |
| :----------- | :---------- | :---------------------------------------------------- |
| **Database** | Global      | A collection of one or more schemas.                  |
| **Schema**   | Logical     | A container for objects like tables, views, and keys. |
| **Relation** | Table-level | The actual table structure and data (rows/columns).   |

### Views vs. Materialized Views

| Feature         | View (Virtual)                                      | Materialized View (Physical)                            |
| :-------------- | :-------------------------------------------------- | :------------------------------------------------------ |
| **Storage**     | Does not store data; only the query definition.     | Stores the actual result of the query on disk.          |
| **Performance** | Slower for complex queries (recomputed every time). | Faster for retrieval (pre-computed).                    |
| **Freshness**   | Always up-to-date with base tables.                 | Can become stale; requires manual or scheduled refresh. |

## 1. Relational Algebra (Procedural)

A set of operations to manipulate relations.

| Operation             |  Symbol   | Description                                                               |
| :-------------------- | :-------: | :------------------------------------------------------------------------ |
| **Selection**         | $\sigma$  | Selects rows satisfying a predicate (Horizontal filtering).               |
| **Projection**        |   $\pi$   | Selects specific columns (Vertical filtering).                            |
| **Union**             |  $\cup$   | Tuples in Relation A OR Relation B (Requires union compatibility).        |
| **Set Difference**    |    $-$    | Tuples in A but NOT in B.                                                 |
| **Cartesian Product** | $\times$  | Combines every tuple of A with every tuple of B.                          |
| **Join**              | $\bowtie$ | Cartesian Product followed by a Selection condition.                      |
| **Division**          |    $/$    | Used for "for all" queries (e.g., Find students who took _all_ subjects). |

## 2. Tuple Calculus (Non-Procedural)

Describes _what_ data to retrieve without specifying _how_.

- **Tuple Relational Calculus (TRC):** Query is of the form $\{ t \mid P(t) \}$.
    - "Find set of tuples $t$ such that predicate $P$ is true for $t$."
- **Domain Relational Calculus (DRC):** Query uses domain variables $\{ <x_1, x_2, ...> \mid P(x_1, x_2, ...) \}$.

## 3. SQL (Structured Query Language)

- **DDL (Data Definition):** `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
- **DML (Data Manipulation):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL (Data Control):** `GRANT`, `REVOKE`.
- **TCL (Transaction Control):** `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

### 3.1. SQL Cheat Sheet

| Clause           | Purpose                   | Example                                       |
| :--------------- | :------------------------ | :-------------------------------------------- |
| **SELECT**       | Choose columns            | `SELECT Name, Age`                            |
| **FROM**         | Specify table             | `FROM Students`                               |
| **WHERE**        | Filter rows (conditions)  | `WHERE Age > 18`                              |
| **GROUP BY**     | Aggregate data            | `GROUP BY Department`                         |
| **HAVING**       | Filter groups             | `HAVING COUNT(*) > 5`                         |
| **ORDER BY**     | Sort results              | `ORDER BY Name ASC`                           |
| **LIMIT / TOP**  | Restrict row count        | `LIMIT 10`                                    |
| **JOIN**         | Combine tables            | `INNER JOIN Courses ON ...`                   |
| **LEFT JOIN**    | All rows from left table  | `LEFT JOIN Grades ON ...`                     |
| **RIGHT JOIN**   | All rows from right table | `RIGHT JOIN Depts ON ...`                     |
| **OUTER JOIN**   | All rows from both tables | `FULL OUTER JOIN Staff ON ...`                |
| **NATURAL JOIN** | Join on matching columns  | `NATURAL JOIN Departments`                    |
| **LIKE**         | Pattern matching          | `WHERE Name LIKE 'A%'`                        |
| **IN**           | Check set membership      | `WHERE ID IN (1, 2, 3)`                       |
| **BETWEEN**      | Range filtering           | `WHERE Age BETWEEN 20 AND 30`                 |
| **IS NULL**      | Check for nulls           | `WHERE Email IS NULL`                         |
| **DISTINCT**     | Remove duplicates         | `SELECT DISTINCT Department`                  |
| **AS**           | Alias for column/table    | `SELECT Name AS StudentName`                  |
| **UNION**        | Combine result sets       | `SELECT ID FROM A UNION SELECT ID FROM B`     |
| **INTERSECT**    | Common tuples in A and B  | `SELECT ID FROM A INTERSECT SELECT ID FROM B` |
| **EXCEPT**       | Tuples in A but not in B  | `SELECT ID FROM A EXCEPT SELECT ID FROM B`    |
| **REFERENCES**   | Define Foreign Key        | `FOREIGN KEY (ID) REFERENCES Parent(ID)`      |
| **Aggregates**   | Math on columns           | `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()` |

### 3.2. SQL Examples

**1. The Basics (Filtering & Sorting)**

Imagine we have a table called `Books`. You want to find specific titles without scrolling through thousands of rows.

- **SELECT / FROM / WHERE:**

    > "Find the title and author of all books published after 2020."

    ```sql
    SELECT Title, Author
    FROM Books
    WHERE PublishYear > 2020;
    ```

- **LIKE / BETWEEN / ORDER BY:**

    > "Find books with 'Harry' in the title, priced between $10 and $20, and sort them by price (cheapest first)."

    ```sql
    SELECT * FROM Books
    WHERE Title LIKE '%Harry%'
    AND Price BETWEEN 10 AND 20
    ORDER BY Price ASC;
    ```

**2. Joins (Connecting the Dots)**

Data is rarely in one table. We usually have a `Users` table and a `Loans` table.

- **INNER JOIN:** Only shows matches. (e.g., "Show me users who currently have a book checked out.")
- **LEFT JOIN:** Shows _everyone_ from the left table, even if they don't have a match on the right.

    > "List all students and any books they have borrowed (even if they haven't borrowed any)."

    ```sql
    SELECT Students.Name, Loans.BookTitle
    FROM Students
    LEFT JOIN Loans ON Students.ID = Loans.StudentID;
    ```

**3. Aggregations (Summarizing Data)**

This is where you turn raw data into "reports."

- **GROUP BY / Aggregates:**

    > "How many books does each author have in our library?"

    ```sql
    SELECT Author, COUNT(*) AS TotalBooks
    FROM Books
    GROUP BY Author;
    ```

- **HAVING:**

    > "Now, only show me authors who have written more than 5 books."
    > _(Note: You use `HAVING` instead of `WHERE` because we are filtering a group, not a single row.)_

    ```sql
    SELECT Author, COUNT(*)
    FROM Books
    GROUP BY Author
    HAVING COUNT(*) > 5;
    ```

**Logical Order of Execution**

It’s helpful to know that SQL doesn't read your code from top to bottom. It actually follows this path:

1. **FROM / JOIN** (Where is the data?)
2. **WHERE** (Filter the raw rows)
3. **GROUP BY** (Aggregate them)
4. **HAVING** (Filter the groups)
5. **SELECT** (Choose the columns to show)
6. **ORDER BY** (Sort the final view)
7. **LIMIT** (Cut off the results)

## 4. Integrity Constraints

Rules to ensure data accuracy and consistency.

1.  **Domain Constraint:** Values in a column must be atomic and from the defined domain.
    - _Example:_ An `Age` column defined as `INTEGER` cannot contain the string "Twenty".
2.  **Entity Integrity:** The **Primary Key** cannot be NULL.
    - _Example:_ In a `Students` table, every student must have a unique `StudentID`; it cannot be left blank.
3.  **Referential Integrity:** A **Foreign Key** value must match a Primary Key in the parent table or be NULL.
    - _Example:_ An `Enrollment` table cannot have a `CourseID` that doesn't exist in the `Courses` table.
4.  **Key Constraints:**
    - **Super Key:** Any set of attributes that uniquely identifies a tuple. (e.g., `{ID, Name}`).
    - **Candidate Key:** Minimal Super Key (no redundant attributes). (e.g., `{ID}`).
    - **Primary Key:** The chosen Candidate Key. (e.g., `ID`).
