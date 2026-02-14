# 01 ER-Model (Entity-Relationship)

A conceptual high-level data model used for database design.

- **Entity:** A real-world object distinguishable from other objects (e.g., `Student`, `Car`).
- **Attribute:** Properties describing an entity.
    - **Simple:** Atomic (e.g., `Age`).
    - **Composite:** Composed of multiple parts (e.g., `Address` -> Street, City).
    - **Derived:** Calculated from other attributes (e.g., `Age` derived from `DOB`).
    - **Multi-valued:** Can have multiple values (e.g., `PhoneNumbers`).
- **Relationship:** Association between entities (e.g., `Student` _EnrolledIn_ `Course`).
    - **Cardinality:** One-to-One (1:1), One-to-Many (1:N), Many-to-One (N:1), Many-to-Many (M:N).
- **Weak Entity:** An entity that cannot be uniquely identified by its own attributes alone. It relies on a **Strong Entity** via an identifying relationship.

## ER Diagram Shapes

| Shape                | Meaning                                                   |
| :------------------- | :-------------------------------------------------------- |
| **Rectangle**        | Entity Set                                                |
| **Double Rectangle** | Weak Entity Set                                           |
| **Ellipse**          | Attribute                                                 |
| **Diamond**          | Relationship Set                                          |
| **Lines**            | Link attributes to entities and entities to relationships |
