## **Year 8: The Architect (Design & Logic)**

**Theme:** Solving the problem before you write the code.

**Skills:** Decomposition, Pattern Recognition, Abstraction, Boolean Logic, Evaluation, Functions.

---

### **Hour 1: Zombie Survival Plan (Decomposition)**

**Concept:** Breaking large, vague problems into small, concrete, manageable sub-problems.

**Activity:** The goal is "Survive a Zombie Apocalypse for 30 Days." Students cannot give vague answers like "Build a base." They must decompose every task into sub-tasks, and those into further sub-tasks until each leaf node is a single, actionable step.

**Example chain:** Survive → Secure Water → Find Source → Check local map for rivers → Walk to nearest river → Test water clarity. Secure Water → Purify → Boil water → Gather firewood → Find dry branches, etc.

**Output:** A hierarchy tree diagram on large paper, decomposing one survival goal into at least 20 atomic sub-tasks. Groups then compare trees and discuss: did different groups decompose the same problem in different ways? Are both valid?

**Key Takeaway:** Decomposition is the first step in solving any complex problem. There is often more than one valid decomposition, but every version must reach steps small enough to actually execute.

---

### **Hour 2: Spot the Pattern (Pattern Recognition)**

**Concept:** Identifying shared structures across different problems so that one solution can be reused.

**Activity:** Present students with three apparently different problems on paper. For example:

* Planning a school trip (choose destination, book transport, collect permission slips, confirm numbers, go).  
* Organising a birthday party (choose venue, arrange transport, send invitations, confirm numbers, go).  
* Setting up a football tournament (choose pitch, arrange travel, send team invitations, confirm entries, go).

**Task:** Students highlight the steps that appear in all three. They then write a single general-purpose algorithm — "Plan an Event" — that captures the common structure using placeholder terms (e.g., "Send communications to attendees" instead of "send invitations" or "collect permission slips").

**Progression:** Give each group a brand new scenario (e.g., organising a charity bake sale). Can they apply their general algorithm to it? Which steps fit perfectly? Which need minor adjustments? This introduces the idea that a recognised pattern becomes a reusable template.

**Key Takeaway:** Pattern recognition lets us avoid solving the same problem from scratch every time. If we spot that two problems have the same shape, we can reuse the same solution structure.

---

### **Hour 3: The Abstract Map (Abstraction)**

**Concept:** Removing unnecessary detail to focus on what matters for a given purpose.

**Activity Part 1 — Maps:** Show a satellite image of the school and surrounding area (overwhelming detail) next to a fire evacuation floor plan (minimal detail, maximum clarity). Discuss: what was removed and why? What would happen if the evacuation map included every tree and car in the car park? Students identify that abstraction means choosing what to keep based on the purpose.

**Activity Part 2 — Simplifying Processes:** Give students a detailed 15-step algorithm for a task they decomposed last lesson (e.g., "Secure Water" from the Zombie plan). Ask them to abstract it into a single named block — `SECURE_WATER` — that hides all 15 steps behind one name. Now the top-level survival plan reads: `SECURE_WATER`, `FIND_SHELTER`, `ESTABLISH_FOOD`. The detail still exists but is hidden until you need it.

**Discussion:** This is exactly how complex systems are managed. You don't need to understand the inner workings of `SECURE_WATER` to use it in the plan — you just need to know what it does, not how it does it. This distinction (interface versus implementation) is one of the most important ideas in computing.

**Key Takeaway:** Abstraction means hiding complexity behind a simpler representation. The detail is not deleted — it is tucked away so you can focus on the bigger picture.

---

### **Hour 4: Logic Gate Human Chain (Boolean Logic)**

**Concept:** AND, OR, NOT gates and Boolean expressions.

**Activity:** Students physically act as logic gates. Two "input" students each hold a card showing TRUE or FALSE. They feed their values to a third student who is the "gate." The gate student has a rule card:

* AND gate: raise your hand only if both inputs are TRUE.  
* OR gate: raise your hand if at least one input is TRUE.  
* NOT gate (one input only): raise your hand if the input is FALSE; lower it if TRUE.

**Progression:** Chain gates together. Two AND gates feed into an OR gate. Change the inputs and trace the output through the chain. Students must predict the final result before the chain acts it out.

**Extension:** Write everyday statements as Boolean expressions. "I will go outside IF it is sunny AND I have finished my homework." What happens if one condition is false? Both? Introduce the idea that every IF statement they wrote in Year 7 was using Boolean logic — they just didn't name it yet.

**Key Takeaway:** All computer decisions reduce to combinations of TRUE and FALSE. Complex conditions are built by chaining simple Boolean operations together.

---

### **Hour 5: The Logic Tournament (Applied Boolean Evaluation)**

**Concept:** Using Boolean logic strategically to evaluate and eliminate options efficiently.

**Activity:** Students play a paper-based version of "Guess Who." Each student has a sheet showing 24 characters with various features. One student secretly picks a character; the other asks yes/no questions to identify them.

**Round 1:** Free play. Students ask whatever questions come naturally. Record how many questions each student needs.

**Analysis:** As a class, examine the questions that were asked. "Does he have blue eyes?" might only eliminate 4 characters. "Is he wearing a hat?" might eliminate 12\. Discuss: what makes a good question? A good question divides the remaining options as evenly as possible.

**Round 2:** Students must write compound Boolean questions. "Does the character have glasses AND a beard?" Now discuss: does combining conditions with AND always help? (It's more specific, so it might eliminate more or fewer depending on distribution.) What about OR? This lets students feel how Boolean operators affect the power of a question.

**Key Takeaway:** Boolean logic is not just a circuit diagram — it's a practical tool for narrowing down possibilities. The quality of your logic determines how quickly you reach an answer.

---

### **Hour 6: The Function Machine (Functions & Parameters)**

**Concept:** Packaging a process as a reusable, named block with inputs and outputs.

**Activity:** Build a physical function machine from a large cardboard box with an "Input" slot and an "Output" slot. A student sits inside — they are the CPU. Feed a number on a slip of paper into the input. The student inside applies a secret rule (e.g., multiply by 2 and add 1\) and pushes the result out.

**Round 1:** The class feeds in several numbers and records the input-output pairs. They must reverse-engineer the function rule from the data.

**Round 2:** Reveal the rule. Now introduce parameters — the function becomes `PROCESS(x, y): output x * y + 1`. Feed in two slips. The student inside applies the rule using both.

**Connection to Abstraction:** Recall Hour 3\. The named blocks `SECURE_WATER` and `FIND_SHELTER` were functions — self-contained processes with a name. Now students see that functions can also take inputs and produce outputs, making them flexible and reusable. A function is abstraction in action.

**Extension:** Give students scenarios: "Write a function called `calculateCost` that takes `price` and `quantity` and returns the total." They define the rule, then swap with another pair and test it by feeding in values.

**Key Takeaway:** Functions are named, reusable blocks of logic. They take inputs, do something predictable, and return outputs. This is how programmers manage complexity — by building small, reliable machines and connecting them together.

