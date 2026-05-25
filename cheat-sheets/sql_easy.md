# SQL Basics Quick Reference

This cheat sheet covers the fundamental commands for interacting with MySQL, managing databases, managing tables, and querying data.

## Server & File Management (Terminal)

*   **Start MySQL Service:** `service mysql start` (Requires root/sudo)
*   **Log into MySQL Shell:** `mysql -u root -p` (Will prompt for password)
*   **Run a SQL script file against a database:**
    ```bash
    cat script.sql | mysql -u root -p database_name
    ```
*   **Importing a Database Dump File:** 
    A SQL dump file usually contains tables and data, but *not* the command to create the database itself. You must create it first!
    1. Create empty database: `echo "CREATE DATABASE db_name;" | mysql -u root -p`
    2. Import the dump: `cat dump_file.sql | mysql -u root -p db_name`

## Database Management

*   **Create a Database safely:** `CREATE DATABASE IF NOT EXISTS db_name;`
*   **Switch to a Database:** `USE db_name;`
*   **Show all Databases:** `SHOW DATABASES;`

## Table Management

*   **Create a Table safely:** 
    ```sql
    CREATE TABLE IF NOT EXISTS table_name (
        column1_name DATATYPE,
        column2_name DATATYPE
    );
    ```
    *Common Datatypes: `INT` (whole numbers), `VARCHAR(X)` (text, X is max length).*
*   **List tables in current database:** `SHOW TABLES;`
*   **View table structure (columns & types):** `DESCRIBE table_name;`
*   **View table creation code (shows Foreign Keys/Linkages):** `SHOW CREATE TABLE table_name;`

## Modifying Data

*   **Insert a new row:** 
    ```sql
    INSERT INTO table_name (col1, col2) VALUES (value1, 'text_value2');
    ```
    *Note: Text strings must be wrapped in single quotes.*

## Querying Data

*   **Select columns:** `SELECT column1, column2 FROM table_name;`
*   **Filter results:** `... WHERE column1 = value;` (or `>`, `<`, `>=`, etc.)
*   **Sort results:** `... ORDER BY column_name ASC;` (Ascending) or `DESC` (Descending)
*   **Limit output (useful for testing):** `... LIMIT number_of_rows;`

## Joins & Aliases (Combining Tables)

*   **Table Aliases:** Rename tables temporarily inside the `FROM` or `JOIN` clause to save typing. If you define a table alias (e.g., `AS t1`), you **must** use it everywhere else in the query.
*   **Column Aliases:** Rename columns for the final output using `AS` in the `SELECT` clause.
*   **INNER JOIN:** Returns only rows where there is a match in *both* tables.
    ```sql
    SELECT a.title, b.genre_id 
    FROM tv_shows AS a
    INNER JOIN tv_show_genres AS b 
    ON a.id = b.show_id;
    ```
*   **LEFT JOIN (with IS NULL filtering):** Used to find records in the left table that have *no match* in the right table (e.g., shows with no genres).
    ```sql
    SELECT a.title 
    FROM tv_shows AS a
    LEFT JOIN tv_show_genres AS b 
    ON a.id = b.show_id
    WHERE b.show_id IS NULL;
    ```

### 🧠 SQL Execution Order
Even though you write a query starting with `SELECT`, SQL processes it in this order:
1. `FROM` / `JOIN` (Gathers tables, establishes table aliases)
2. `WHERE` (Filters rows)
3. `GROUP BY` (Aggregates rows)
4. `HAVING` (Filters aggregated rows)
5. `SELECT` (Picks output columns, establishes column aliases)
6. `ORDER BY` (Sorts final data)
7. `LIMIT` (Truncates final data)

## Functions & Aggregation

*   **Aggregate Functions:** `AVG(column)` calculates average, `MAX(column)` finds the highest value.
*   **Rename Output Columns (Alias):** `SELECT AVG(score) AS calculated_average ...`
*   **Group By (Aggregating per category):** 
    When you want averages/maximums *per category* (e.g., max temp per state), you must use `GROUP BY`.
    ```sql
    SELECT category_column, MAX(value_column) AS top_value
    FROM table_name
    GROUP BY category_column;
    ```

## Advanced: Programming in SQL (Triggers, Procedures, Functions)

When writing multi-statement blocks of code in SQL, you must temporarily change the statement delimiter from `;` to `$$` so MySQL doesn't execute the code prematurely.

### 1. Triggers (Automatic Actions)
Automatically fire when an `INSERT`, `UPDATE`, or `DELETE` happens on a table.
*   **`NEW.column`**: Access the incoming data for an INSERT/UPDATE.
*   **`OLD.column`**: Access the existing data before an UPDATE/DELETE.

```sql
DELIMITER $$
CREATE TRIGGER decrease_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END $$
DELIMITER ;
```

### 2. Stored Procedures (Callable Scripts)
Like a function in programming. It can take inputs, hold complex logic (like `IF` and `SELECT ... INTO var`), and modify data.

```sql
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN score INT)
BEGIN
    DECLARE my_var INT; -- You can declare variables!
    -- Run complex logic, IF statements, and multiple UPDATEs/INSERTs here
END $$
DELIMITER ;
-- To run it: CALL AddBonus(1, 100);
```

### 3. User-Defined Functions (Return a Value)
Similar to procedures, but they **must return a single value** and can be used directly inside standard `SELECT` queries. If it only does math and doesn't edit tables, add `DETERMINISTIC`.

```sql
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END $$
DELIMITER ;
-- To use it: SELECT SafeDiv(10, 2);
```

## Syntax Reminders

*   Always end SQL statements with a semicolon `;`
*   Single line comments start with `-- ` (Followed by a space).
*   String values need `'single quotes'`. Table and column names usually do not need them unless they contain strange characters.