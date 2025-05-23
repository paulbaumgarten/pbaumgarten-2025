---
title: Being organised
parent: Internal assessment
layout: default
nav_order: 3
---

# Internal assessment: Organisational strategies
{: .no_toc }

{: .highlight }
For the new IB Diploma Computer Science syllabus to start teaching in August 2025, and for first examinations in May 2027.

- TOC
{:toc} 

Context:  
*For many of you, this is your first substantial programming project that will take  more than an hour or two to complete. The idea may be daunting \- where to start?\! The aim of this guide is to help offer some strategies.*

# Pre-planning

Preparing your success criteria and some design diagrams in advance of programming are not just an idealistic nice-to-have, they actually help you think through your project and identify the key components required. 

Before you start programming you should have (at a minimum)...

* 8 to 10 success criteria \- each of which identifies a key function your project needs to perform. Specify how you will measure completion of each criterion.  
* Sketches of the visuals (user interface, screen navigation flow) \- annotate key features such as buttons, fields, animation / movement / interaction  
* UML of the main classes you may create \- identify the variables you are going to need to keep track of in each class  
* Flowchart or pseudocode logic overview \- what happens when your program is executed? From clicking 'start', what does the program do? When does it move to a 'new screen' or perform a calculation? What are the key decisions and algorithms involved and when?

Turn your success criteria into a set of categories for a task check-list of to-dos and milestones.

* What are the different features you need for each success criteria?  
* Each feature becomes a goal for your progress checklist  
* Examples:  
  * Flask: “Login system”, “Data storage”, “Form submission & validation”  
  * Pygame: “Character movement”, “Collision detection”, “Score tracking”

When you have your progress check-in's with me, I will ask: Which phase are you on? Which feature are you on?

# Organise your tools

* Create a Github account and a repository for your Internal Assessment  
* Add me as a collaborator to the repository  
* Install Github Desktop on your computer, and clone the repository  
* Github Desktop will allow you to synchronise a dedicated project folder on your computer to the Github cloud \- acting as a remote backup, and a way of sharing your work in progress.  
* For academic integrity purposes, please use Github Desktop at least once a week when doing your intensive programming time.

# Phase 1: Foundations

Start with the basics \- get your project functional and then build on it.

For example:

* Pygame \- Get a basic game loop running  
* Flask \- Get a basic website with one route running

Test your environment is working correctly.

# Phase 2: Minimum viable product (MVP)

If everything else fell apart, what is the absolute core of your project? Get that functional first\! ie: Identify the primary, most important feature and implement that. Test the primary feature and only move on once it works. 

Keep your code simple and avoid overcomplicating it. Use fake data or placeholder images where needed \- focus on functionality for now, don't get distracted by details like making it pretty.

For example

* Pygame: Create your playable character (as a block) and some basic game mechanics (movement, collision)  
* Flask: Basic CRUD (create-read-update-delete) operations for the main component of the project

# Phase 3: Develop additional features incrementally

Gradual development helps avoid feeling overwhelmed at the scope of your project, and makes debugging easier.

Add one feature at a time, test each thoroughly as you go, before moving on to the next. Prioritise features based on their importance to your success criteria.

For example:

* Pygame: Add enemies, scoring, new levels, game save/load, bots, multiplayer features  
* Flask: Add additional routes, authentication system, database integration one step at a time

# Phase 4: User interface and user experience (UI/UX)

Make the project user friendly and show your attention to detail. These are the "nice to have"s but not essential to the functionality of your project.

Implement UI buttons, menus, forms; make the project visually appealing, add some animations and slick transitions; test with peers and gather feedback.

# Phase 5: Testing and debugging

Ensure the project is functional, meets your success criteria, and is free of significant bugs.

* Test each feature against the success criteria  
* Test for edge cases and unexpected user inputs  
* Use unit-testing for key functions and classes