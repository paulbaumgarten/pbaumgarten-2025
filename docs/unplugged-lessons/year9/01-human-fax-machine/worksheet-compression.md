# Compression Worksheet — Run-Length Encoding

**Name:** _________________________________ **Date:** _____________

---

## Part 1: Understanding RLE

RLE replaces runs of repeated values with a count and the value.

**Format:** `(count, value)` — e.g., `(3,0)` means three zeros.

**Example:** `0 0 0 1 1 1 1 0 0`
→ RLE: `(3,0)(4,1)(2,0)`
→ Original: 9 values. RLE: 6 numbers. Compression ratio: 9/6 = **1.5:1**

**Practice — encode these sequences:**

a) `1 1 1 1 1 1 1 1` → RLE: _____________ Original: 8, RLE: ___, Ratio: ___

b) `0 1 0 1 0 1 0 1` → RLE: _____________ Original: 8, RLE: ___, Ratio: ___

c) `0 0 0 0 1 1 0 0` → RLE: _____________ Original: 8, RLE: ___, Ratio: ___

**Which of a, b, c compresses best? Which compresses worst? Why?**

_______________________________________________________________

---

## Part 2: Encode the Checkerboard (Image 3) in RLE

**Row 1 binary:** ■□■□■□■□ = ___,___,___,___,___,___,___,___

**Row 1 RLE:** _______________

**How many RLE numbers for Row 1?** ___

**Total RLE numbers for the full checkerboard** (all 8 rows): ___

**Original bits:** 64. **RLE numbers needed:** ___. **Compression ratio:** ___:1

Is this good compression? ___

---

## Part 3: Encode the Solid Block (Image 4) in RLE

**Row 1 binary:** □□□□□□□□ = _,_,_,_,_,_,_,_ → RLE: _____________ (numbers needed: ___)

**Row 2 binary:** □■■■■■■□ = _,_,_,_,_,_,_,_ → RLE: _____________ (numbers needed: ___)

**How many unique row types are there in this image?** ___

**Total RLE numbers for the full solid block** (all 8 rows): ___

**Compression ratio:** 64 / ___ = ___:1

---

## Part 4: Comparison

| Image | Original bits | RLE numbers needed | Compression ratio |
|-------|:-------------:|:------------------:|:-----------------:|
| Checkerboard | 64 | | |
| Solid Block | 64 | | |

**Which image compressed better?** _______________________________________________

**What type of image compresses well with RLE?** _______________________________________________

**What type of image compresses poorly?** _______________________________________________

---

## Part 5: Real World

**Why do photos of blank documents (like a printed page) transmit quickly by fax?**

_______________________________________________________________

**Why does JPEG compression work better on landscape photos than on photos of a TV showing static?**

_______________________________________________________________

**RLE is "lossless" — the original can be perfectly reconstructed. What would "lossy" compression mean? Can you think of an example?**

_______________________________________________________________

_______________________________________________________________
