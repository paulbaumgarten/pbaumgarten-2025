---
title: "Unit 8: Capstone Project"
layout: default
nav_order: 8
parent: MicroPython Course
has_children: true
has_toc: false
---

# Unit 8: Capstone Project
{: .no_toc }

You've learned variables, loops, lists, functions, files, and the full hardware kit. Now it's time to put it all together into a complete game — **Dodge** — a real-time action game running on the 8×8 NeoPixel grid.

## What is Dodge?

Dodge is a game where:
- A **player dot** sits at the bottom of the grid
- **Obstacles** fall from the top one column at a time
- The player moves **left and right** using two buttons to avoid obstacles
- Each obstacle dodged scores a point
- A collision ends the game — the best score is saved to a file
- Difficulty increases over time (obstacles fall faster)

## Lessons in This Unit

| Lesson | Title | What You Build |
|--------|-------|---------------|
| [Lesson 22](lesson-22-capstone-setup.html) | Capstone Setup | Static display, player movement (Milestones 1–2) |
| [Lesson 23](lesson-23-capstone-game.html) | The Game Loop | Falling obstacles, collision, scoring (Milestones 3–4) |
| [Lesson 24](lesson-24-capstone-polish.html) | Polish and Beyond | High scores, title screen, difficulty, full code review |

## How This Unit Works

Unlike previous lessons, there is **no pre-written guided walkthrough to copy**. Instead, each lesson gives you:
- A milestone specification (what the game should do)
- Hints and starter code fragments
- Guided questions to help you think through the logic

You will write the game incrementally — each milestone adds one feature and builds on the previous.

{: .highlight }
This is your chance to be the programmer, not just a follower. Use everything you've learned. Look back at previous lessons when you need a reminder. Ask for help when genuinely stuck — but try the problem first.

## Hardware Needed

- ESP32-S3 (built-in NeoPixel GPIO 48 not used for game display)
- WS2812B 8×8 NeoPixel grid (GPIO 6)
- Two buttons: Left button GPIO 0, Right button GPIO 14 (both to GND, PULL_UP)

## The Milestone Roadmap

| Milestone | Feature |
|-----------|---------|
| 1 | Grid initialises, player dot appears at bottom-centre |
| 2 | Buttons move player left and right |
| 3 | Obstacles fall from top; new obstacle spawns when previous one reaches bottom |
| 4 | Collision detection — game over when player hit |
| 5 | Score displayed on the single built-in NeoPixel (colour changes by score); high score saved to file |
| 6 | Title screen, speed increases, game-over flash, restart without reboot |

## Tips for Success

- **Build incrementally.** Get Milestone 1 working before starting Milestone 2.
- **Test often.** Run the code after every small change.
- **Read error messages.** They tell you exactly what went wrong and which line.
- **Use print() for debugging.** Print your variables to understand what's happening.
- **Look things up.** Previous lessons are your reference manual.
