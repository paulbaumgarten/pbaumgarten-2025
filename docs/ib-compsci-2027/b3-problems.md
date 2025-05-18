
### Problem Set 1: Input/Print  

Focus: Basic I/O, string literals.  

1. Greeting Bot  
   - *Scenario*: Ask the user for their name and print a greeting.  
   - *Example 1*:  
     Input: `Alice`  
     Output: `Hello, Alice!`  
   - *Example 2*:  
     Input: `Bob`  
     Output: `Hello, Bob!`  
   - Save as: `exercise-1-1.py`

2. Age Echo  
   - *Scenario*: Prompt the user for name and their age and repeat it back.  
   - *Example 1*:  
     Input: `Alice`  
     Input: `25`  
     Output: `Hello, Alice! You are 25 years old.`  
   - *Example 2*:  
     Input: `Bob`  
     Input: `17`  
     Output: `Hello, Bob! You are 17 years old.`  
   - Save as: `exercise-1-2.py`

3. Favorite Color  
   - *Scenario*: Prompt the user for their name and their favorite color.  
   - *Example 1*:  
     Input: `Alice`  
     Input: `blue`  
     Output: `Hello, Alice! Your favorite color is blue.`  
   - *Example 2*:  
     Input: `Bob`  
     Input: `green`  
     Output: `Hello, Bob! Your favorite color is green.`  
   - Save as: `exercise-1-3.py`

---

### Problem Set 2: Numbers  
Focus: Arithmetic operations, numeric types.  

1. Circle Area  
   - *Scenario*: Input a float as a radius, calculate the area of a circle, print to 2 decimal places.
   - *Example*:  
     Input: `5`  
     Output: `Area = 78.54`  
   - Save as: `exercise-2-1.py`

2. Temperature Converter  
   - *Scenario*: Input an integer. Print the first three multiples of that number.  
   - *Example*:  
     Input: `5`  
     Output: `Multiples of 5 are 5 10 15`  
   - Save as: `exercise-2-2.py`

3. Odd or Even  
   - *Scenario*: Input an integer. Print whether it is even or odd.
   - *Example 1*:  
     Input: `4`  
     Output: `Even`  
   - *Example 2*:  
     Input: `7`  
     Output: `Odd`  
   - Save as: `exercise-2-3.py`

4. Digit Sum  
   - *Scenario*: Print the sum of digits of an input 2-digit number.  
   - *Example*:  
     Input: `45`  
     Output: `9`  
   - Save as: `exercise-2-4.py`

---

### Problem Set 3: Strings  
Focus: String manipulation, slicing, methods.  

1. Reverse a String  
   - *Scenario*: Print the reverse of a hardcoded string (without loops or if statements).  
   - *Example*:  
     Input: `"hello"`  
     Output: `olleh`  
   - Save as: `exercise-3-1.py`

2. Initials  
   - *Scenario*: Print initials from an input full name.  
   - *Example*:  
     Input: `"John Doe"`  
     Output: `JD`  
   - Save as: `exercise-3-2.py`

3. Substring Check  
   - *Scenario*: Print `True` if a substring exists in a string.  
   - *Example*:  
     Input: `"strawberry", "berry"`  
     Output: `True`  
   - *Example*:  
     Input: `"apple", "berry"`  
     Output: `False`  
   - Save as: `exercise-3-3.py`

4. Replace 'a's  
   - *Scenario*: Replace all the 'a' characters with the '@' symbol in a string.  
   - *Example*:  
     Input: `"Hi, how are you today?"`  
     Output: `Hi, how @re you tod@y?`  
   - Save as: `exercise-3-4.py`

---

### Problem Set 4: Exceptions  
Focus: `try/except`, input validation.  

1. Integer Input  
   - *Scenario*: Ask for an integer; handle non-integer inputs.  
   - *Example 1*:  
     Input: `abc`  
     Output: `Invalid input!`  
   - *Example 2*:  
     Input: `3.14`  
     Output: `Invalid input!`  
   - *Example 3*:  
     Input: `42`  
     Output: `Valid: 42`  
   - Save as: `exercise-4-1.py`

2. Division Guard  
   - *Scenario*: Divide two numbers; handle division by zero (output divisions to 1dp).  
   - *Example 1*:  
     Input: `5, 0`  
     Output: `Cannot divide by zero!`  
   - *Example 2*:  
     Input: `10, 2`  
     Output: `5.0`  
   - Save as: `exercise-4-2.py`

3. Age Validator  
   - *Scenario*: Ensure age is a positive integer.  
   - *Example 1*:  
     Input: `-5`  
     Output: `Age must be positive!`  
   - *Example 2*:  
     Input: `20`  
     Output: `Valid age: 20`  
   - Save as: `exercise-4-3.py`

4. Number Parser  
   - *Scenario*: Convert user input to float; handle `ValueError`.  
   - *Example 1*:  
     Input: `3.14`  
     Output: `Valid float: 3.14`  
   - *Example 2*:  
     Input: `abc`  
     Output: `Invalid float!`  
   - Save as: `exercise-4-4.py`

---

### Problem Set 5: Lists  
Focus: List operations, indexing, methods.  

For all of these questions, the list will be input as a string using space separation. You can input it as a list using the following:

```python
# Input a list of strings
my_list = input().split(" ")
# Input a list of integers
my_list = [int(x) for x in input().split(" ")]
```

1. Sum of List  
   - *Scenario*: Print the sum of a list of numbers.  
   - *Example*:  
     Input: `1 2 3`  
     Output: `6`  
   - Save as: `exercise-5-1.py`

2. List Reversal  
   - *Scenario*: Reverse a list without using `reverse()`.  
   - *Example*:  
     Input: `4 5 6`  
     Output: `[6, 5, 4]`  
   - Save as: `exercise-5-2.py`

3. Element Check  
   - *Scenario*: Print `True` if a second input exists in a list.  
   - *Example 1*:  
     Input 1: `10 20 30`  
     Input 2: `20`  
     Output: `True`  
   - *Example 2*:  
     Input 1: `10 20 30`  
     Input 2: `24`  
     Output: `False`  
   - Save as: `exercise-5-3.py`

4. List Concatenation  
   - *Scenario*: Combine two lists.  
   - *Example*:  
     Input 1: `1 2`  
     Input 2: `3 4`  
     Output: `[1, 2, 3, 4]`  
   - Save as: `exercise-5-4.py`

---

### Problem Set 6: Stacks  
Focus: LIFO operations, `append()`/`pop()`.  

1. Stack Push/Pop  
   - *Scenario*: Simulate stack operations on a hardcoded list.  
   - *Example*:  
     Input: `Push 5, Push 3, Pop`  
     Output: `[5]`  

2. Parentheses Checker  
   - *Scenario*: Check if a hardcoded string has balanced parentheses.  
   - *Example 1*:  
     Input: `"(())"`  
     Output: `True`  
   - *Example 2*:  
     Input: `"(()"`  
     Output: `False`  

3. Undo Mechanism  
   - *Scenario*: Simulate "undo" using a stack of actions.  
   - *Example*:  
     Input: `["write", "delete", "undo"]`  
     Output: `["write"]`  

4. Reverse a List  
   - *Scenario*: Reverse a hardcoded list using a stack.  
   - *Example*:  
     Input: `[1, 2, 3]`  
     Output: `[3, 2, 1]`  

5. Decimal to Binary  
   - *Scenario*: Convert a hardcoded number to binary using a stack.  
   - *Example*:  
     Input: `10`  
     Output: `101