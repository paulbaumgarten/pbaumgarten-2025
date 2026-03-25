---
title: "Unit 7: The Grid"
layout: default
nav_order: 7
parent: MicroPython Course
has_children: true
has_toc: false
---

# Unit 7: The Grid
{: .no_toc }

You've used the single built-in NeoPixel since Lesson 1. Now it's time to upgrade to the full 8×8 NeoPixel grid — 64 individually addressable RGB LEDs you can draw on like a tiny screen.

## Lessons in This Unit

| Lesson | Title | Key Concepts |
|--------|-------|-------------|
| [Lesson 19](lesson-19-2d-lists.html) | Two-Dimensional Lists | 2D lists, double indexing, nested loops, creating grids |
| [Lesson 20](lesson-20-neopixel-grid.html) | The 8×8 NeoPixel Grid | Grid wiring, framebuffer, row×col to index, pixel art |
| [Lesson 21](lesson-21-grid-animations.html) | Grid Animations | Animation loops, velocity, bouncing, rain, spinner patterns |

## New Hardware: WS2812B 8×8 NeoPixel Grid

64 individually addressable RGB LEDs in an 8×8 matrix. Each LED has its own controller chip. Controlled via a single data pin using the same `neopixel` module you already know.

## What You'll Be Able to Do by the End

- Create and manipulate 2D lists (lists of lists)
- Access grid cells with double indexing `grid[row][col]`
- Map row/column coordinates to NeoPixel index
- Use a framebuffer for flicker-free animation
- Display pixel art, patterns, and animations

{: .highlight }
This unit brings everything together — loops, lists, functions, and hardware. The grid is your canvas. By the end of this unit, you'll be ready to build the capstone project.
