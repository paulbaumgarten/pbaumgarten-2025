# Algorithm Reference Card — Keep This Visible While Sorting

---

## BUBBLE SORT

**Idea:** Compare adjacent pairs and swap them if they're in the wrong order. Larger values "bubble" to the right.

**Steps:**
1. Start at the FIRST card (position 1). Compare it to the card in position 2.
2. If the LEFT card is BIGGER: SWAP them. If not: leave them.
3. Move one position right. Compare positions 2 and 3.
4. Keep comparing and swapping until you reach the last pair. This is ONE PASS.
5. After each pass, the rightmost unsorted card is now in its final position — ignore it next pass.
6. Repeat from step 1 until a full pass makes NO swaps.

**Example with [4, 2, 3, 1] — first pass:**
- Compare 4,2: swap → [2,4,3,1]
- Compare 4,3: swap → [2,3,4,1]
- Compare 4,1: swap → [2,3,1,4] ← 4 is now in position

---

## SELECTION SORT

**Idea:** Find the smallest remaining item and place it in its correct position.

**Steps:**
1. Scan ALL cards. Find the SMALLEST.
2. SWAP it to position 1.
3. Now ignore position 1 (it's sorted). Scan remaining cards for the NEXT smallest.
4. SWAP it to position 2.
5. Repeat until all cards are placed.

**Example with [4, 2, 3, 1]:**
- Round 1: scan all, find 1, swap with position 1 → [1, 2, 3, 4]... (lucky data)
- Round 2: scan positions 2–4, find 2 (already in place) → no swap needed

---

## INSERTION SORT

**Idea:** Take each card and slide it left into its correct position among already-sorted cards.

**Steps:**
1. Consider the SECOND card. Compare it to cards to its LEFT.
2. If the card to the LEFT is BIGGER: shift it right one space, continue moving left.
3. When you find a smaller card (or reach the start): place your card here.
4. Move to the THIRD card. Repeat.
5. Continue until the last card is placed.

**Example with [4, 2, 3, 1] — inserting position 2:**
- Card = 2. Look left: 4 > 2, shift 4 right → [_, 4, 3, 1]. Place 2 → [2, 4, 3, 1].
- Card = 3. Look left: 4 > 3, shift right → [2, _, 4, 1]. 2 < 3, stop. Place 3 → [2, 3, 4, 1].
