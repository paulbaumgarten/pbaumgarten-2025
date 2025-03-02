---
title: Log files
parent: Python notes
layout: default
nav_order: 6
---

# Log files

Instead of filling your code with print() function calls just for debugging purposes, it may be helpful to put program output into a text file you can read through later.

At the start of your program, import logging and create the log file.

```py
import logging
logging.basicConfig(filename='myproject.log', level=logging.DEBUG)
```

Whenever you want to add a line to the file, use logging.info(), logging.debug() or logging.error()…

```py
logging.info(f"Program started {datetime.now()}") # Log an info message
logging.debug(f"this is a debug message")         # Log a debug message
logging.debug(f"The value of num: {num}")
logging.error(f"A major error occurred")          # Log an error message
```

Quick example

```py
from datetime import datetime
import logging

logging.basicConfig(filename='myproject.log', level=logging.DEBUG)
logging.info(f"Program started {datetime.now()}")

for i in range(10):
    logging.debug(f"The value of i is {i}")

print("Program finished")
```

Content of the resulting log file

```
INFO:root:Program started 2022-05-26 14:26:12.249657
DEBUG:root:The value of i is 0
DEBUG:root:The value of i is 1
DEBUG:root:The value of i is 2
DEBUG:root:The value of i is 3
DEBUG:root:The value of i is 4
DEBUG:root:The value of i is 5
DEBUG:root:The value of i is 6
DEBUG:root:The value of i is 7
DEBUG:root:The value of i is 8
DEBUG:root:The value of i is 9
```

