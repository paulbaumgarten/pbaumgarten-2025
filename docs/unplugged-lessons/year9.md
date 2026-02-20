## **Year 9: The Data Scientist (Data & Optimisation)**

**Theme:** Representing information and making things fast.

**Skills:** Data Representation (Binary), Compression, Searching, Sorting, Graph Theory, Algorithmic Complexity.

---

### **Hour 1: The Human Fax Machine (Binary & Images)**

**Concept:** How computers represent images using binary data and pixels.

**Activity:** Give Student A a grid (8×8 or larger) with a simple pixel drawing — a smiley face, an arrow, a letter. Give Student B an identical but blank grid. They sit back to back.

**Task:** Student A must transmit the image using only 1s and 0s, row by row. "Row 1: 0, 0, 1, 1, 1, 1, 0, 0." Student B fills in the grid. Compare results — any errors in transmission become visible immediately.

**Extension — Compression:** Transmitting 64 individual digits is slow. Introduce Run-Length Encoding: instead of "0, 0, 0, 0, 0, 1, 1, 0" say "five 0s, two 1s, one 0." Count how many values each method requires. Students calculate the compression ratio and discuss when RLE works well (large blocks of same colour) versus when it doesn't (checkerboard patterns).

**Key Takeaway:** All digital images are grids of numbers. Compression reduces the amount of data without losing the information, but its effectiveness depends on the content.

---

### **Hour 2: The Number Hunt (Searching Algorithms)**

**Concept:** Linear search versus binary search and why strategy matters.

**Activity:** Play "Guess my number between 1 and 100."

**Round 1 — Linear approach:** Students guess randomly or sequentially. Tally the number of guesses needed. Several students play, and results are recorded on the board.

**Round 2 — Binary search:** Teach the strategy. Always guess the middle of the remaining range. Start at 50\. "Higher." Guess 75\. "Lower." Guess 62\. Each guess halves the remaining possibilities. Students play again using this method. Tally the guesses.

**Analysis:** Graph both sets of results. Linear search needed up to 100 guesses. Binary search never needed more than 7\. Discuss why — each guess eliminates half the remaining options, and halving 100 seven times gets you to 1\.

**Discussion:** Binary search only works if the data is in order. What if the numbers were jumbled? You'd have to sort them first — which is what the next lessons address.

**Key Takeaway:** The strategy you use to search matters enormously. Binary search is dramatically faster, but it requires sorted data as a precondition.

---

### **Hour 3: The Sorting Race (Sorting Algorithms Compared)**

**Concept:** Different algorithms solve the same problem at different speeds.

**Activity:** Prepare sets of 10 numbered cards. Three teams each receive an identical shuffled set and must sort them into order — but each team must follow a different algorithm:

**Team 1 — Bubble Sort:** Compare the first two cards. If they're in the wrong order, swap them. Move to the next pair. Repeat from the start until no swaps are needed in a full pass.

**Team 2 — Selection Sort:** Scan all cards, find the smallest, place it first. Scan the remaining cards, find the smallest, place it second. Repeat.

**Team 3 — Insertion Sort:** Take cards one at a time from the unsorted pile. Insert each card into the correct position within a growing sorted pile.

**Timed race:** All three teams start simultaneously. Record how long each takes and how many comparisons/swaps each required (teams keep a tally).

**Discussion:** Which was fastest? Which felt easiest to follow? Which would scale worst with 100 cards or 1,000? Introduce the idea that efficiency is not about one run but about how performance changes as the problem grows.

**Key Takeaway:** There are many ways to solve the same problem. Some approaches scale far better than others. Choosing the right algorithm is as important as getting the right answer.

---

### **Hour 4: The Sorting Network (Parallel Processing)**

**Concept:** Tasks can sometimes be done simultaneously rather than one at a time.

**Activity:** Draw a sorting network on the playground or gym floor using chalk or tape — a set of parallel lines with "comparator" nodes where two lines meet.

**Action:** Six students start at one end, each holding a randomly assigned number card. They walk along the lines. Whenever two students meet at a comparator, they compare numbers. The student with the lower number takes the left path; the higher number takes the right. By the end of the network, all six emerge in perfect sorted order.

**The key insight:** No single person was "in charge." No one saw all the numbers at once. The sorting emerged from many small, local comparisons happening independently — and some of them happened at the same time on different parts of the network.

**Connection to Hour 3:** The sorting algorithms from last lesson were sequential — one comparison at a time, one team doing all the work. The sorting network allows parallel operations. Discuss: modern computers have multiple cores. This is why.

**Key Takeaway:** Parallel processing means doing multiple operations simultaneously. It is fundamentally different from doing things faster in sequence, and it enables performance gains that no single-threaded optimisation can match.

---

### **Hour 5: The Map Problem (Graph Theory & Networks)**

**Concept:** Many real-world problems can be modelled as nodes connected by edges.

**Activity:** Give each group a map of a fictional island with 8–10 towns connected by roads. Each road has a distance or travel time written on it. Not all towns are directly connected.

**Task 1 — Shortest path:** Find the shortest route from Town A to Town H. Students quickly discover that the most direct-looking route is not always the shortest — a longer-looking path through more towns can have a lower total distance.

**Task 2 — The delivery problem:** A delivery driver must visit every town exactly once and return to the start. Find the shortest possible tour. Groups attempt this by trial and error and record their best route. Compare across groups — did anyone find the optimal solution? How do they know it's optimal?

**Discussion:** Reveal that Task 2 is a version of the Travelling Salesman Problem — one of the most famous problems in computer science. For 10 towns, there are over 3 million possible routes. For 20 towns, more routes than atoms in the universe. Some problems are easy to check but astonishingly hard to solve. This is a genuine unsolved question in mathematics and computing.

**Connection:** Relate to real life — sat-nav routing, delivery logistics, network design, social network analysis. Graphs are everywhere.

**Key Takeaway:** Graph theory gives us a way to model connected systems. Some graph problems can be solved efficiently; others are so hard that even the fastest computers cannot guarantee the best answer in a reasonable time.

---

### **Hour 6: The Complexity Olympics (Algorithmic Efficiency & Evaluation)**

**Concept:** Bringing together everything from the year to evaluate and compare algorithmic approaches.

**Activity:** Set up a series of timed stations, each revisiting a concept from the year. At each station, students face a choice between two approaches — one efficient, one naive.

**Station 1 — Search:** Find a name in an alphabetical list of 64 names. Method A: start from the top and work down. Method B: open to the middle and use binary search. Time both.

**Station 2 — Sort:** Sort 15 cards. Method A: bubble sort. Method B: insertion sort. Count comparisons.

**Station 3 — Compress:** Transmit a pixel grid. Method A: send every digit. Method B: use run-length encoding. Count how many values are sent.

**Station 4 — Route:** Find the shortest route across a small graph. Method A: try the first route you see. Method B: systematically try all routes and compare. Discuss the trade-off between speed of decision and quality of result.

**Synthesis:** Gather as a class. For each station, discuss: which method was faster? Which was more reliable? Were there cases where the "worse" method was actually acceptable? Introduce the idea that algorithmic thinking is not about always finding the single best solution — it is about understanding the trade-offs and making an informed choice.

**Key Takeaway:** Efficiency is not one thing. It involves time, space, reliability, and complexity. The mark of computational thinking is not memorising the best algorithm but having the tools to evaluate and choose wisely.

