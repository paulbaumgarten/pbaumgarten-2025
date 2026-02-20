**Year 7: The Instruction Manual (Algorithmic Precision)**

**Theme:** Computers are literal — they do exactly what you tell them, nothing more.

**Skills:** Algorithms, Sequence, Variables, Iteration, Selection, Flowcharts, Debugging, Nested Structures.

---

### **Hour 1: The "Robot" Teacher (Sequence & Precision)**

**Concept:** Precision and sequential execution.

**Activity:** The class writes a program (a numbered list of instructions) to get you, the teacher, to perform a simple task such as making a jam sandwich or putting on a blazer.

**The Catch:** You act as a completely literal robot. If they say "put the bread on the plate" but the bread is in a bag, you place the entire bag on the plate. If they say "pick up the knife," you grab it by the blade. Every ambiguity is exploited.

**Key Takeaway:** Implied knowledge does not exist in computing. Every assumption must be made explicit. What feels obvious to a human must still be spelled out for a machine.

---

### **Hour 2: The Memory Box (Variables & State)**

**Concept:** Named containers that store values which can change over time.

**Activity:** Each student is given a mini whiteboard or a piece of card. Each board is labelled with a variable name: `score`, `lives`, `playerName`. You call out instructions and students update their boards accordingly.

**Sequence example:**

* SET `score` TO 0  
* SET `lives` TO 3  
* SET `score` TO `score` \+ 10  
* SET `lives` TO `lives` \- 1  
* What is `score` now? What is `lives` now?

**Progression:** Introduce a scenario — a simple text adventure. "You find a coin. SET `score` TO `score` \+ 5." Students trace through a short story, updating their boards at each step. Then compare final values. Anyone who lost track has experienced a common programming bug: losing track of state.

**Key Takeaway:** A variable is a named box. It holds one value at a time. When you assign a new value, the old one is gone.

---

### **Hour 3: The Loop Dance (Iteration)**

**Concept:** For loops and while loops.

**Activity:** Students design a short dance routine, but instead of writing out every individual step, they must use loop notation.

**For loop example:** `REPEAT 4 TIMES: [Clap, Stomp]`

**While loop example:** `WHILE music is playing: [Wave hands]`

**Progression:** Combine with variables. Introduce a counter: `SET count TO 0. WHILE count < 8: [Step left, Step right, SET count TO count + 1]`. Students physically act it out, updating a whiteboard counter each time through the loop. They can see the counter climbing toward the exit condition.

**Key Takeaway:** Loops save effort and reduce repetition. A while loop depends on a condition, which often depends on a variable changing — connecting this hour directly to the previous one.

---

### **Hour 4: The Maze Game (Selection & Flowcharts)**

**Concept:** IF/ELSE decisions and visual flow control.

**Activity:** Mark out a grid on the floor using masking tape. Place coloured cards face-down on certain squares as obstacles or triggers. Students write a set of instructions to navigate a blindfolded partner (the "bot") from one corner to the opposite corner.

**Progression:** Introduce conditional cards. When the bot steps on a square containing a card, they flip it. "IF card is Red, turn Right. ELSE IF card is Blue, turn Left. ELSE, move Forward." Students must plan for all possibilities.

**Flowchart introduction:** After the first attempt, teach simple flowchart notation — rectangles for processes, diamonds for decisions, arrows for flow. Students redraw their maze solution as a flowchart. This gives them a visual tool for representing branching logic that they can carry forward.

**Key Takeaway:** Programs make decisions. Flowcharts let us see the shape of those decisions before we write code.

---

### **Hour 5: Bug Hunters (Debugging & Testing)**

**Concept:** Finding, diagnosing, and fixing errors is a core programming skill.

**Activity:** Provide students with pre-written algorithms that contain deliberate bugs. These could include:

* A sandwich-making algorithm where the steps are out of order (sequence error).  
* A maze solution where a loop repeats one too many times (off-by-one error).  
* A set of instructions that says "IF card is Red, turn Left" when the flowchart clearly shows it should turn Right (logic error).

**Task:** Students work in pairs. They trace through each broken algorithm step by step, identify the bug, name what type of error it is, and write the corrected version.

**Extension:** Pairs then write their own deliberately buggy algorithm and swap with another pair to debug. This is surprisingly hard — writing a convincing bug requires understanding the concept thoroughly.

**Key Takeaway:** Bugs are normal and expected. The skill is not avoiding them entirely but finding and fixing them systematically. Tracing through code line by line is the most reliable debugging tool.

---

### **Hour 6: The Grand Challenge (Nested Structures & Synthesis)**

**Concept:** Combining loops, selection, and variables — including structures inside other structures.

**Activity:** A new, more complex maze. This time, the maze has a repeating section — a corridor where the same pattern of obstacles appears multiple times. Students must navigate their bot through the full maze, but they are given a strict line limit for their solution. The only way to meet the limit is to use a loop that contains a decision inside it.

**Example solution structure:**

```
REPEAT 3 TIMES:
    Move Forward
    IF wall ahead:
        Turn Right
        Move Forward
        Turn Left
```

**Progression:** Award points for correctness first, then efficiency (fewest lines), then adaptability (would the same code work if the maze changed slightly?). This final criterion introduces the idea that good algorithms generalise.

**Key Takeaway:** Real programs combine structures inside other structures. A loop can contain a decision. A decision can contain another decision. Understanding nesting is the bridge between unplugged thinking and real code.

