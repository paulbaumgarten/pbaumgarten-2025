---
title: Y09 Smart plant pots 2
parent: MYP Digital Design
layout: default
nav_order: 5
---

# Smart plant pots 2 (Year 9 Digital Design)

* SOI: Social entrepreneurs can innovate and influence communities.
* Key concept: Communities
* Related concept: Innovation
* Context: Fairness and development (social entrepreneurs)
* Technology: ESP32, MicroPython, Pump, Moisture sensor, Temperature sensor, Wifi, IoT

Use your social entrepreneurial skills to construct an innovative, smart pot planter to nurture your plants.

---

**Criterion C: Creating the solution**

| Level | What You Need to Do | Self-assessment and peer feedback Checklist |
| :---- | :---- | :---- |
| **1–2** | \* I showed only a little skill when building or coding my system. \* My system doesn’t work properly or is incomplete. \* I didn’t really plan out my steps. | I created a clear step-by-step plan for building and coding my smart pot plant. My plan includes what I will do, when I will do it, and what materials or tools I’ll need. My plan is easy to follow and could be used by someone else to build a similar system. I connected the hardware (moisture sensor, pump, ESP32, etc.) correctly and safely. I wrote working MicroPython code that controls the system based on sensor readings. I tested my system regularly and fixed any technical problems I found. I followed my plan closely and made sure my system works as intended. My smart pot automatically waters the plant and sends updates to a phone or app. I documented any changes I made to my original plan or design. I clearly explained why I made those changes and how they helped improve the system. |
| **3–4** | \* I made a plan, but it was missing details or hard to follow. \* I built a basic system that works a little bit, but not fully. \* I used some coding and wiring skills, but had difficulty. \* I briefly said what I changed during the project. |  |
| **5–6** | \* I created a clear step-by-step plan that most people could follow. \* I used good skills to wire and code my system. \* My system works the way I planned and is put together neatly. \* I explained the changes I made and why I made them. |  |
| **7–8** | \* I created a well-organized and realistic plan that shows how I used my time and materials efficiently. \* I used excellent skills to build and program my system. \* I followed my plan carefully and built a smart plant pot that works well and looks professional. \* I clearly explained the changes I made as I worked and gave good reasons for them |  |

**Criterion D: Evaluating**

| Level | What You Need to Do | Self-assessment and peer feedback Checklist |
| :---- | :---- | :---- |
| **1–2** | \* I described a simple test to check if my system works. \* I said whether my system was successful or not, but didn’t explain much. | I created a good set of tests to check if my system works as expected.  I collected useful data from my tests (e.g. sensor readings, watering times, notifications).  I used my test results to check how well my system met the original goals and design.  I explained clearly what worked well and what could be better.  I suggested realistic ways to improve my system (e.g. better design, smarter code, more efficient watering).  I explained how my smart plant pot helps the user (e.g. saves time, makes plant care easier).  I explained how my system supports sustainability (e.g. saves water, promotes greenery at home or school).  I thought about how this type of system could help other people or the environment in the real world. |
| **3–4** | \* I used a test that gave me useful data (like moisture levels or notifications). \* I compared my results to my original goals and said how successful it was. \* I listed some ways I could improve my system. \* I briefly said how my system might help someone or make a difference. |  |
| **5–6** | \* I used a few good tests to collect data that showed if my system worked. \* I described in detail how successful it was based on the results. \* I explained some good ideas for how to improve it. \* I described how my system could help the user or the environment. |  |
| **7–8** | \* I used strong and detailed testing methods that gave accurate results (e.g. moisture logs, watering times, notifications). \* I explained clearly how well my system met the goals using the data. \* I gave thoughtful and realistic suggestions to improve the system. \* I explained how my system could make a positive difference for people and the environment. |  |

---

## Schedule

| \# | Content | Learning process |  |  |
| :---- | :---- | :---- | :---- | :---- |
|  |  | Learning experiences and teaching strategies | Formative assessment | Differentiation |
| 1 | Unit Launch \+ Big Ideas | Explore the statement of inquiry and key concepts (communities, innovation). Use think-pair-share to unpack the statement of inquiry:Social entrepreneurs can innovate and influence communities. Watch short video clips or case studies from the maker community as a powerful example of innovation in action, especially in education, sustainability, and digital design Facilitate a **gallery walk** of examples. Innovation is the practical implementation of ideas that result in the introduction of new goods or services or improvement in offering goods or services. How are programming and electronics tools of innovators?  Discuss how self-watering planters could aid our local communities (e.g., lack of green space, food insecurity, busy lifestyles). Use a **graphic organizer** for students to brainstorm user needs and community challenges.  |  |  |
| 2 | Intro to ESP32 \+ IDE setup | Install Thonny, connect ESP32, run simple print statements Control the onboard Neopixel |  |  |
| 3 | Python Basics 1Hello Python\! – Variables & Output | Python understandings: Instructions followed in sequence Syntax quirks: Indentation, casing Variables: Defining, assigning, calculating print() function Turtle basics Neopixel color setting Challenges Create a name tag that prints your name, age, and favorite color. Use Turtle to draw your initials. Light your Neopixel with your favorite color Change your Turtle pen color using a variable. | Mini coding exercises | Self-selecting different exercises based on confidence levels  Video walkthroughs available for selected exercises for those who need it |
| 4 | Python Basics 2Loops & Patterns | Python understandings: for loops range() Patterns with Turtle Blinking Neopixel Challenges Use a loop to draw a spiral or flower pattern with Turtle. Blink your Neopixel 5 times in your favorite color. Animate a pattern in Turtle and match it with a light color. Create a rainbow effect with your Neopixel using a loop. Make a Turtle pattern with 100+ lines that changes color every few steps. | Mini coding exercises | Self-selecting different exercises based on confidence levels  Video walkthroughs available for selected exercises for those who need it |
| 5 | Python Basics 3Conditionals & Functions | Python understandings if, elif, else Functions (defining & calling) Mood-based logic Drawing \+ lighting based on input Challenges Write an if statement that prints a message based on the temperature. Create a function that lights the Neopixel based on your mood. Draw an emoji or symbol with Turtle based on a mood variable. Add more moods and colors to your function. Let the program choose a random mood each time it runs. | Mini coding exercises | Self-selecting different exercises based on confidence levels  Video walkthroughs available for selected exercises for those who need it |
| 6 | Python Basics 4 Skills Mastery | Mini exercises and challenges to gain confidence with Python Draw an equilateral triangle using Turtle. Extension: Try a hexagon or pentagon\! Print a countdown from 5 to 1 using a loop. Extension: Add time.sleep(1) to make it a real countdown\! Extension: Blink the Neopixel to indicate the passage of each second Extension: Have the Neopixel change from blinking green to orange and then red as the countdown gets closer to zero\! TODO: Devise additional exercises  C.ii. demonstrate excellent technical skills | Mini coding exercises | Self-selecting different exercises based on confidence levels  |
|  | CNY BREAK |  |  |  |
| 7 | Components Overview | ESP32 Moisture sensors Pump,  Relay to control pump LiPo battery and charging unit | "Debug the circuit" activity – students identify and fix a broken circuit diagram Quick group challenge or Kahoot quiz |  |
| 8 | Wiring & Testing | MicroPython and wiring requirements for: Relay and pump Water tank sensor Soil moisture sensor  |  | Scaffolded code templates (e.g. with comments or gaps to fill) for those who need it |
| 9 | Mounting in Pot | Install electronics into 3D-printed pot |  | Video walkthroughs available for those who need it Peer support |
| 10 | Mounting in Pot | Install electronics into 3D-printed pot C.ii. demonstrate excellent technical skills when making the solution C.iii. follow the plan to create the solution, which functions as intended |  | Peer support |
| 11 | Full System Code | Integrate pump \+ sensor logic: if soil dry, water the plant |  | Video walkthroughs available for those who need it |
|  | APRIL BREAK |  |  |  |
| 13 | Full System Code | Integrate pump \+ sensor logic: if soil dry, water the plant C.ii. demonstrate excellent technical skills when making the solution C.iii. follow the plan to create the solution, which functions as intended |  |  |
| 14 | Adding IoT | Send moisture/temp data via WiFi to phone (e.g. [ntfy.sh](http://ntfy.sh)) C.ii. demonstrate excellent technical skills when making the solution C.iii. follow the plan to create the solution, which functions as intended |  | Video walkthroughs available for those who need it |
| 15 | Testing & Debugging | Test entire system: sensor → logic → pump → feedback C.ii. demonstrate excellent technical skills when making the solution C.iii. follow the plan to create the solution, which functions as intended |  |  |
| 16 | Peer Testing Day | Exchange systems, run peer feedback sessions. Collect feedback. ATL: Communication Skills: Provide respectful, meaningful feedback During peer testing and code walkthrough reviews. Structure peer feedback sessions using sentence starters: “One thing I liked was...”, “One thing you could improve is...” Model giving feedback on sample code (e.g. clarity, efficiency). Use sticky notes or Google Docs comments to provide non-verbal feedback. D.i generate data, to measure the success of the solution | Peer review rubric |  |
| 17 | Dragon's den pitch | Create a 90-120 second Dagon's Den style pitch: Introduce the need in your community (refer back to unit 1 design requirements) Showcase your design (refer back to unit 1 design requirements) Showcase your solution (demonstrate functionality of your product) Share the reviews and feedback D.ii. critically evaluate the success of the solution against the design specification D.iv. explain the impact of the solution on the client/target audience. |  |  |
| 18 | Dragon's den pitch | Create a 90-120 second Dagon's Den style pitch: Introduce the need in your community (refer back to unit 1 design requirements) Showcase your design (refer back to unit 1 design requirements) Showcase your solution (demonstrate functionality of your product) Share the reviews and feedback D.ii. critically evaluate the success of the solution against the design specification D.iv. explain the impact of the solution on the client/target audience. |  |  |
| 19 | Reflection | What changed from the plan? Why? What was learned? Thinking skills: Generate multiple new ideas, solutions and inquiries  During improvements and extensions. Encourage “What if?” thinking: “What if your plant was outdoors? What if you added a light sensor?” Invite students to brainstorm 3 ways to improve water efficiency or notification systems. C.iv. fully justify changes made to the chosen design and plan when making the solution. D.iii. explain how the solution could be improved |  |  |
| 20 | FINALISE ARR | Last opportunity to finalise any assessment details |  |  |


