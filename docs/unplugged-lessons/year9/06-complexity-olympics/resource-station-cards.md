# Complexity Olympics — Station Cards

**Laminate and place at each station before the lesson.**

---

## STATION 1: O(1) — CONSTANT TIME

### Event: Direct Lookup

**Your task:** Someone calls out a position number. Find that card directly.

**Setup:** Take a stack of numbered cards, laid out in order.

**Procedure:**
1. Someone calls out a number (e.g., "card 7")
2. Go directly to that position. Pick it up.
3. Count the steps: always **1 step**, no matter how many cards there are.

**Try it for:**
- Stack of 10 cards → steps needed: ___
- Stack of 100 cards → steps needed: ___
- Stack of 1,000 cards → steps needed: ___

**Record on your worksheet!**

**The Point:** This is what an array index does — `cards[7]` retrieves the value in exactly 1 step, whether the array has 10 or 10,000 items. A dictionary key lookup is also O(1).

---

## STATION 2: O(log n) — LOGARITHMIC TIME

### Event: Binary Search

**Your task:** Find a target number in a sorted stack using binary search.

**Target number is on the sticky note at this station.**

**Procedure:**
1. Lay out your sorted cards in order.
2. Always check the MIDDLE card.
3. If middle = target: done!
4. If target is higher: take the top half. Repeat.
5. If target is lower: take the bottom half. Repeat.
6. Count every time you check a card.

**Try it for:**
- 8 cards (target = 6th card) → guesses: ___
- 16 cards (target = 11th card) → guesses: ___
- 32 cards (target = 25th card) → guesses: ___

**The Point:** Every time you double the input, you only need ONE more guess. log₂(8)=3, log₂(16)=4, log₂(32)=5.

---

## STATION 3: O(n) — LINEAR TIME

### Event: Finding the Maximum

**Your task:** Find the highest-valued card in a shuffled pile.

**Procedure:**
1. Shuffle your cards face-down.
2. Turn them over one at a time.
3. Keep track of the highest value seen so far.
4. When you've looked at every card, you've found the maximum.
5. Count how many cards you looked at.

**Try it for:**
- n=5 cards → cards looked at: ___
- n=10 cards → cards looked at: ___
- n=20 cards → cards looked at: ___

**The Point:** You must look at every card at least once. Double the input = double the work. There's no shortcut — you can't skip any card when finding a maximum in an unsorted collection.

---

## STATION 4: O(n²) — QUADRATIC TIME

### Event: Finding All Duplicate Pairs

**Your task:** Check every card against every other card.

**Procedure:**
1. Take n cards.
2. Compare card 1 to card 2, card 3, card 4... (n-1 comparisons)
3. Compare card 2 to card 3, card 4... (n-2 comparisons)
4. Continue until all pairs checked.
5. Count every comparison.

**Prediction formula:** comparisons = n × (n−1) ÷ 2

**Try it for:**
- n=3 → predicted: ___, actual: ___
- n=4 → predicted: ___, actual: ___
- n=5 → predicted: ___, actual: ___
- n=6 → predicted: ___, actual: ___

**Warning:** For n=10, this is 45 comparisons. For n=100: 4,950. For n=1,000: 499,500.

**The Point:** Double the input = FOUR TIMES the work. This grows very fast — quadratic growth is impractical for large datasets.
