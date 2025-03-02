---
title: Postgressql databases
parent: Python notes
layout: default
nav_order: 6
---

# Postgresql database
{: .no_toc }

- TOC
{:toc} 

Installation

```
pip install psycopg2-binary
```

Import

```py
import psycopg2
import psycopg2.extras
```

Database connection string

The format of a _postgressql_ database connection string is as follows. You will need this string to be able to connect. Typically it is loaded from a secure file, or pulled in from the external environment. For security reasons, it should never be hard-coded into your Python files, except possibly when you are in the early stages of development using test values that will change later.

```
postgresql://username:password@host:port/database
```

As a side note, if you had an external environment values of `DATABASE_URL`, the `os` library provides a means for you to easily retrieve it...

```py
# Will have a value of None if the environment variable does not exist
connection_string = os.getenv("DATABASE_URL")

# Will generate an exception if the environment variable does not exist
connection_string = os.env["DATABASE_URL"]
```

### Writing to a database

```py
import psycopg2

conn = psycopg2.connect(os.env["DATABASE_URL"])
conn.autocommit = True 
with conn.cursor() as cur:
    sql = """CREATE TABLE IF NOT EXISTS people (
        email TEXT PRIMARY KEY,
        familyName TEXT,
        givenName TEXT,
        preferredName TEXT,
        school TEXT,
        schoolType TEXT,
        schoolYear TEXT,
        meal TEXT,
        security TIMESTAMP,
        registration TIMESTAMP,
        points INTEGER
    );"""
    print("people table created")
    cur.execute(sql)
conn.close()
```

### Reading from a database

```py
import psycopg2

conn = psycopg2.connect(os.env["DATABASE_URL"])
conn.autocommit = True 
with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    sql = "SELECT * FROM people WHERE (name = %s)"
    parameters = (name,) # A tuple in matching order as required by the SQL string
    cur.execute(sql, paramaters)
    data = cur.fetchall()
    for i,record in enumerate(data):
        print(f"The {i}th record was {record}")
conn.close()
```

* The `cursor_factory=psycopg2.extras.DictCursor` setting instructs _postgres_ to return the dataset as a list of dictionaries. Personally I find this much more convienant to work with than tuples.

