---
title: "Unit 2: Making Decisions"
layout: default
nav_order: 2
parent: MicroPython Course
has_children: true
has_toc: false
---

# Unit 2: Making Decisions
{: .no_toc }

Your programs so far have run the same way every time. This unit changes that — you'll learn to write programs that can choose different paths based on conditions. You'll also connect your first external component: a push button.

## Lessons in This Unit

| Lesson | Title | Key Concepts |
|--------|-------|-------------|
| [Lesson 5](lesson-05-selection.md) | Selection with if and else | if, else, comparison operators (==, !=, <, >, <=, >=) |
| [Lesson 6](lesson-06-buttons-and-elif.md) | Buttons and elif | elif, push button wiring, active-low inputs, debouncing |
| [Lesson 7](lesson-07-logical-operators.md) | Logical Operators | and, or, not, truth tables, complex conditions |

## New Hardware: Push Buttons

You'll wire your first external component — a push button. Buttons connect a GPIO pin to GND when pressed, giving you physical input beyond the keyboard.

## What You'll Be Able to Do by the End

- Write programs that take different actions based on conditions
- Handle multiple choices with `elif`
- Read a physical button and respond to it in code
- Combine multiple conditions using `and`, `or`, and `not`
- Build a two-button controller for the NeoPixel

{: .highlight }
Selection is one of the most important ideas in all of programming. After this unit, your programs can make real decisions — and that changes everything.
