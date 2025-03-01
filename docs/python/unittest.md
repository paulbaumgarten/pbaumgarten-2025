# Python unittest Cheatsheet

Unit tests check if the different parts (units) of a larger program work correctly. It is like testing individual Lego pieces before building something with them.

## Setup

```python
import unittest
from unittest.mock import patch
```

## Example 1 - Testing input/output on the main function

Given a Python file called `my_project.py`:

```python
a = int(input())
b = int(input())
answer = a + b
print(a+b)
```

Construct this test file:

```python
import unittest
from unittest.mock import patch
import sys
from io import StringIO

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3'])
    def test_main(self, mock_input):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Run your project code
        exec(open('my_project.py').read())
        
        # Assert the output
        self.assertEqual(captured_output.getvalue().strip(), '5')
        
        # Reset output to normal
        sys.stdout = sys.__stdout__
```

## Example 2 - Testing input/output in a function

Given a Python file called `my_project.py`:

```python
def adder():
    a = int(input())
    b = int(input())
    answer = a + b
    print(a+b)
```

Construct this test file:

```python
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from my_project import adder  # Import the adder function from your project

class TestAdderFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3'])
    def test_adder(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        adder()  # Call the imported function
        
        self.assertEqual(captured_output.getvalue().strip(), '5')
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
```

## Example 3 - Testing function parameters and return values

Given a Python file called `my_project.py`:

```python
def adder(a, b):
    answer = a + b
    return answer
```

Construct this test file:

```python
import unittest
from my_project import adder  # Import the adder function from your project

class TestAdderFunction(unittest.TestCase):
    def test_adder(self):
        result = adder(2, 3)  # Call the imported function
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

## Example 4 - Testing object oriented programming

Given a Python file called `my_project.py`:

```python
class Adder:
    def __init__(self, initialise):
        self.__total = initialise
    
    def add(self, value):
        self.__total = self.__total + value
    
    def get_total(self):
        return self.__total
```

Construct this test file:

```python
import unittest
from my_project import adder  # Import the adder function from your project

class TestAdderFunction(unittest.TestCase):
    def test_adder(self):
        result = adder(2, 3)  # Call the imported function
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```