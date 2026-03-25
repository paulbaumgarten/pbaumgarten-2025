
# Project Brief: Self-Paced MicroPython Course for Pre-IB Student

## Context & Audience

Design a complete, self-paced introductory programming course for a single student: a motivated 15-year-old who is about to start the IB Diploma Computer Science course. She has NO prior formal programming experience but is enthusiastic about both programming and hardware/electronics. Her classmates will have completed 2 years of IGCSE Computer Science, so the goal is to build her confidence and foundational skills to match that level — specifically in Python programming fundamentals (the IB CS course does NOT require OOP or abstract data types at this stage).

Design this new course using MicroPython running on ESP32-S3 microcontrollers. Every lesson should involve physical hardware so that learning programming concepts is always tied to tangible, visible, real-world outputs. This is deliberate — the hardware makes abstract concepts concrete and keeps motivation high.

The student will work through this independently over several months (approximately 10–12 weeks, a few hours per week), with occasional check-ins from her teacher. Lessons must therefore be clearly written, self-contained, and assume no prior knowledge unless taught in a previous lesson. Include troubleshooting tips where common mistakes are likely.

## Hardware & Components Available

The student has access to the following. Introduce components progressively — don't overwhelm early lessons with too many components at once:

- **ESP32-S3 development board** (has a BUILT-IN single NeoPixel on the board — use this for early lessons before introducing external components)
- **Raspberry Pi Pico** (can be used as an alternative or introduced later)
- **Breadboard and jumper wires**
- **Push buttons** (momentary, active-low with pull-up resistors or using internal pull-ups)
- **IR sensors** (digital output, detects proximity/reflection)
- **HC-SR04 ultrasonic distance sensors** (requires trigger/echo pins, returns distance)
- **9G micro servos** (PWM controlled, 0–180 degrees)
- **3.3V relay modules** (to switch 5V geared DC motors on/off)
- **5V geared DC motors** (controlled via the relay)
- **WS2812B NeoPixel 8x8 grid** (64 individually addressable RGB LEDs, controlled via a single data pin)

## Programming Concepts to Cover (in this approximate sequence)

Each concept must be formally introduced, explained, and then applied in a hardware project:

1. **Python fundamentals** — syntax rules, indentation, comments, `print()`, variables, basic expressions. (Note: `input()` works differently in MicroPython on microcontrollers — substitute physical inputs like buttons where appropriate, but DO teach the concept of `input()` and explain how it works in standard Python / the REPL, and have the student use it via the Thonny console)
2. **Built-in data types** — `int`, `float`, `bool`, `str`. Type conversion. String operations (concatenation, slicing, `.upper()`, `.lower()`, `.find()`, `len()`).
3. **Selection** — `if`, `elif`, `else`, comparison operators, logical operators (`and`, `or`, `not`), nested conditions.
4. **Iteration** — `while` loops, `for` loops, `range()`, `break`, `continue`, nested loops.
5. **1D lists** — creating lists, indexing, slicing, `.append()`, `.remove()`, `len()`, iterating through lists, list of sensor readings.
6. **2D lists** — lists of lists, accessing elements with double indexing, iterating with nested loops. This maps directly to the 8x8 NeoPixel grid.
7. **Writing functions** — defining functions with `def`, parameters, `return` values, scope (local vs global), calling functions, functions that call other functions.
8. **Reading and writing text files** — `open()`, `.read()`, `.readline()`, `.readlines()`, `.write()`, `with` statements, CSV-style data. Use cases: logging sensor data, loading configuration, saving high scores.

**Explicitly NOT required:** Object-oriented programming (classes), abstract data types (stacks, queues, trees, linked lists). Do not teach these.

## Course Structure

Generate the course as a series of lessons organised into topics. Aim for approximately **20–24 lessons**. Each topic should focus on a programming concept cluster and introduce one or two new hardware components.

### For EACH lesson, generate:

1. **Lesson title** and estimated time (most lessons should be 45–90 minutes)
2. **Learning objectives** (2–4 clear, specific objectives per lesson)
3. **Concept explanation** — clear prose explanation of the programming concept with annotated code examples. Use analogies and plain language. Remember the student is 15 and has no background — don't be patronising but don't assume knowledge.
4. **Hardware setup** — if new hardware is introduced, include a clear wiring description (pin connections in a table format). Describe what to connect where. Include a note about double-checking connections before powering on.
5. **Guided walkthrough** — a step-by-step coding activity where the student builds a working program. Show the code in stages, not all at once. Explain every new line. Include expected output/behaviour ("When you run this, you should see the LED turn green for 1 second, then red for 1 second").
6. **Challenges** — 2–3 extension tasks of increasing difficulty (labeled: ⭐ Core, ⭐⭐ Extension, ⭐⭐⭐ Stretch). These should require the student to modify or extend the guided walkthrough code, applying the concepts independently.
7. **Common mistakes & debugging tips** — a short section addressing likely errors (e.g., "If your servo is jittering, check that you're not calling the angle-set function in a tight loop without a sleep").
8. **Key vocabulary** — a brief list of programming terms introduced in that lesson with one-line definitions.

### Suggested Unit Progression (adapt as you see fit, but cover all concepts):

- **Unit 1: Getting Started** — Setting up Thonny IDE, connecting the ESP32-S3, the REPL, first programs using the built-in NeoPixel. Covers: print, variables, data types, basic expressions.
- **Unit 2: Making Decisions** — Introduce buttons as physical input. Covers: selection (if/elif/else), boolean logic, comparison operators.
- **Unit 3: Loops & Repetition** — LED patterns, animation on the built-in NeoPixel, introduce IR sensor. Covers: while loops, for loops, range(), break, continue.
- **Unit 4: Collections of Data** — Introduce ultrasonic sensor. Store sensor readings in lists. Covers: 1D lists, list operations, iterating over lists.
- **Unit 5: Functions & Modularity** — Introduce servos. Write reusable functions to control hardware. Covers: defining functions, parameters, return values, scope.
- **Unit 6: Working with Files** — Log sensor data to files, read configuration files. Introduce relay + motor. Covers: file reading, file writing, CSV parsing.
- **Unit 7: The Grid** — Introduce the 8x8 NeoPixel grid. 2D lists to represent the grid state. Covers: 2D lists, nested loops, mapping list indices to pixel positions.
- **Unit 8: Capstone Project** — A simple game on the 8x8 NeoPixel grid using buttons for input. This should integrate most concepts learned: functions, loops, selection, 2D lists, file I/O (for high scores). Provide a structured project guide, not just "make a game" — scaffold it with milestones.

### Capstone Project Guidance

The capstone should be a simple game displayed on the 8x8 NeoPixel grid with button controls. Suitable game ideas (student can choose or the course can guide one):
- **Snake** — classic snake game, player dot moves around grid eating food dots, body grows
- **Dodge** — player dot at bottom, obstacles fall from top, avoid them, score increases with time
- **Breakout** — simplified single-row paddle at bottom, ball bounces, break blocks at top
- **Memory match** — light up a sequence, player must repeat it using buttons

The project should be broken into milestones:
1. Display a static pixel on the grid
2. Move a pixel with button input
3. Add game elements (food/obstacles/targets)
4. Add scoring and game-over logic
5. Add file I/O for high scores
6. Polish: add colour, animation, difficulty progression

## Output Format

Generate each lesson as a separate Markdown file. Use this naming convention:
- `unit-1/lesson-01-hello-micropython.md`
- `unit-1/lesson-02-variables-and-types.md`
- etc.

Also generate:
- `README.md` — course overview, what you'll learn, what you need, how to use this course
- `SETUP-GUIDE.md` — detailed guide to installing Thonny, connecting the ESP32-S3/Pico, flashing MicroPython firmware if needed, running a first test program
- `HARDWARE-REFERENCE.md` — quick-reference wiring guide for each component used in the course
- `unit-X/challenges/` — for any challenge solution files (Python), so the student can check their work if stuck

Ensure the final markdown files are compatible for publishing on a Jekyll website.

## Tone & Style

- Friendly, encouraging, and clear. Not patronising.
- Use "you" to address the student directly.
- Celebrate small wins ("Run your code — you should see your LED blink! You just wrote your first embedded program.").
- When introducing jargon, always define it immediately.
- Use real-world analogies to explain abstract concepts.
- Include occasional "Did you know?" sidebars connecting what they're learning to real-world applications (e.g., "The ultrasonic sensor you're using works on the same principle as how bats navigate in the dark").
- Remind the student periodically that making mistakes and debugging is a normal, important part of programming — not a sign of failure.

## Technical Notes

- Use **MicroPython** (not CircuitPython) throughout.
- Use the **Thonny IDE** as the development environment.
- For NeoPixel control, use the `neopixel` module built into MicroPython.
- For the ESP32-S3 built-in NeoPixel, note the specific GPIO pin is 48.
- For servos, use PWM via the `machine` module.
- For ultrasonic sensors, either write a simple trigger/echo function from scratch (good learning exercise) or use a lightweight module — prefer writing from scratch so the student learns about timing and digital I/O.
- Pin numbers should be clearly stated but also explain that the student may need to adjust pin numbers for their specific board.
- Always include `import time` / `from time import sleep` early and use appropriate delays in loops to avoid overwhelming the hardware.
- Include a brief explanation of what "flashing" firmware means and why microcontrollers work differently from running Python on a laptop.

Now generate the complete course.
