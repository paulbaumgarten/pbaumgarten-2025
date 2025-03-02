---
title: SQLite databases
parent: Python notes
layout: default
nav_order: 6
---

# SQLite database
{: .no_toc }

- TOC
{:toc} 

```py
import sqlite3
```

The following `database_write()` and `database_read()` functions will simplify the process of performing basic SQL operations for those fairly new to programming. I recommend you add these to your code.

```py
filename = "your_database.db"

def database_write(sql, data=None):
    connection = sqlite3.connect(filename)
    connection.row_factory = sqlite3.Row
    db = connection.cursor()
    if data:
        rc = db.execute(sql, data).rowcount
    else:
        rc = db.execute(sql).rowcount
    connection.commit()
    db.close()
    connection.close()
    return rc # Number of rows affected

def database_read(sql, data=None):
    connection = sqlite3.connect(filename)
    connection.row_factory = sqlite3.Row
    db = connection.cursor()
    if data:
        db.execute(sql, data)
    else:
        db.execute(sql)
    records = db.fetchall()
    rows = [dict(record) for record in records]
    db.close()
    connection.close()
    return rows # List of dictionaries
```

Examples of how the above functions can be used to read or write to a database.

* `database_read()` returns a list of dictionary objects.
* `database_write()` returns an integer indicating how many rows were added or edited.

```py
records = database_read("SELECT * FROM people;")
affected = database_write("UPDATE people SET name='test';")
```

There are many security risks associated with including user provided values directly into the SQL string like the above. Instead, you are urged to create a dictionary containing fields of the user provided values and then use “parameters” in the SQL string (ask your teacher about these).

```py
# Example using dictionary of values as data parameter
info = {"id":1, "given":"Paul", "familyname":"Baumgarten"}
database_write("UPDATE people SET name=:given, surname=:familyname WHERE id=:id;", info)
```
 
Example SQL to create a new table

```sql
CREATE TABLE 'person' (
    'id'            INTEGER AUTOINCREMENT,
    'givenName'     TEXT,
    'familyName'    TEXT,
    'email'         TEXT NOT NULL,
    PRIMARY KEY('id')
);
```

Example SQL to modify records

```sql
-- Insert a record
INSERT INTO table (field, field, ...) VALUES (value, value, ...);

-- Update one or more records
UPDATE table SET field=value, field=value WHERE field=value;

-- Delete one or more records
DELETE FROM table WHERE field=value;
```

Example SQL to query existing records

```sql
-- Get every field of every record from a table.
SELECT * FROM table;

-- Get some fields for every record from a table.
SELECT field, field, field FROM table;

-- Get records that match where field is set to value.
SELECT * FROM table WHERE field = value;

-- Get records sorted by field
SELECT * FROM table WHERE field=value ORDER BY field2;

-- Get first 10 records
SELECT * FROM table WHERE field=value ORDER BY field2 LIMIT 10;

-- Get records that match where two fields have set values.
SELECT *…* FROM table WHERE (field = value) AND (field = value);

-- Get records that match where two possible field/values exist.
SELECT * FROM table WHERE (field = value) OR (field = value);

-- Get records from two tables
SELECT * FROM (table1 LEFT JOIN table2 ON table1.f1=table2.f2) WHERE table1.f3=value;
```

