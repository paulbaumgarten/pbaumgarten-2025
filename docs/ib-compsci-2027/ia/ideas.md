---
title: IA Algorithms and ideas
parent: IB Computer Science 2027
layout: default
nav_order: 3
---

# Algorithms and ideas for the IA
{: .no_toc }

{: .highlight }
For the new IB Diploma Computer Science syllabus to start teaching in August 2025, and for first examinations in May 2027.

- TOC
{:toc} 

The Internal Assessment prioritises the design, construction and use of algorithms. 

If you struggle to even know what algorithms exist, the following is a list to help you get started. 

## Foundations

* **Stacks or Queues**
    * *Undo/Redo Feature in a Text Editor:* Using a stack-based command history.
    * *Print Job Scheduler:* Using a queue for managing print requests.
    * *Balanced Parentheses Checker:* Using a stack for syntax validation.
    * *BFS/DFS Implementation:* Using a queue/stack explicitly for traversal.

* **Binary Search Trees (BSTs)**
    * *Dictionary/Spell Checker:* Enabling fast word lookup and insertion.
    * *Student Grade Tracker:* Managing insert, search, and delete records efficiently.
    * *Auto-complete System:* Facilitating prefix-based searches (though Tries are also common).
    * *Leaderboard System:* Allowing efficient ranking updates and retrieval.

* **Priority Queue**

* **Sets**
    * *Spell Checker:* Quickly checking if a word exists in a dictionary (membership testing).
    * *Social Media "Mutual Friends" Finder:* Using set intersection to find common connections.
    * *Duplicate File Detector:* Comparing file hashes to detect identical files.

* **Object-Oriented Programming (OOP)**
    * *Library Management System:* Modeling Books, Users, and Loans as interconnected objects.
    * *Bank Account Simulator:* Representing Accounts, Transactions, and Customers with classes and methods.
    * *E-commerce Product Catalog:* Organizing Products, Categories, and Reviews using inheritance and composition.
    * *Game Character System:* Using inheritance for different enemy types with shared and unique behaviors.

* **Recursion and backtracking**

* **Greedy algorithms**

## Searching and sorting

* **Timsort** (Hybrid Sorting Algorithm)
    * *Standard Library Sorting:* Used in Python and Java's default sort functions; it's a stable, highly-optimized blend of Merge Sort and Insertion Sort.
* **Counting Sort / Radix Sort** (Non-Comparison Sorting)
    * *High-Speed Data Processing:* Sorting large lists of integers or strings where the values are restricted to a small range, achieving $O(n+k)$ complexity, far faster than $O(n \log n)$ comparison sorts in specific cases.

## Matricies

* **Multidimensional Arrays**
    * *Minesweeper Game:* Storing board state and revealing adjacent cells.
    * *Chess/Checkers Board:* Tracking piece positions and legal moves.
    * *Pixel Art Editor:* Storing RGB values in a 2D grid.
    * *Matrix Operations Calculator:* Handling addition, multiplication, and determinant calculations.

## Graph and Tree Algorithms

* **Depth First Search (DFS)**
    * *Maze Solver:* Finding a path from start to end by exploring as deeply as possible.
    * *File System Traversal:* Simulating directory structure search.
    * *Sudoku Solver:* Using backtracking to fill valid numbers.
    * *Dependency Resolver:* Using topological sorting for task scheduling (e.g., build systems).

* **Breadth First Search (BFS)**
    * *Shortest Path in a Grid:* Finding the shortest path in a maze with unweighted edges.
    * *Social Network Friend Finder:* Finding degrees of separation (e.g., 6 degrees of separation).
    * *Web Crawler Simulation:* Visiting links level by level.
    * *Puzzle Solver (e.g., 8-Puzzle):* Finding optimal moves by exploring all neighbors uniformly.

* **Dijkstra / A star** (Shortest Path Finding)
    * *Pathfinding Visualizer:* Creating an interactive grid with obstacles.
    * *Public Transport Route Planner:* Finding shortest routes considering travel time and transfers.
    * *RPG Game Enemy AI:* Allowing smart movement around obstacles in a game world.
    * *Drone Delivery Simulator:* Optimizing delivery paths for maximum efficiency.

* **Prim's or Kruskal's Algorithm** (Minimum Spanning Tree)
    * *Utility Network Design:* Finding the cheapest way to lay fiber optic cable or water pipes to connect a set of cities or houses.

* **Floyd-Warshall Algorithm** (All-Pairs Shortest Path)
    * *Mapping Services:* Calculating the shortest distance between *every* pair of nodes/locations in a small transport network.

* **Topological Sort** (Kahn's or DFS-based)
    * *Course Pre-requisites:* Ordering university courses so a student takes required pre-requisites before advanced courses.

* **Trie (Prefix Tree)**
    * *Phonebook Search:* Storing and quickly searching contacts/words based on their prefix (used in older T9 phone input).

* **Max Flow / Min Cut** (e.g., Edmonds-Karp)
    * *Logistics/Resource Allocation:* Maximizing the flow of resources (e.g., oil, internet traffic) through a network with limited capacities.

## Optimization and Dynamic Programming

* **The Knapsack Problem** (Dynamic Programming)
    * *Cargo Loading Optimization:* A spacecraft or delivery truck deciding which items to take to maximize value without exceeding a weight limit.
* **Bellman-Ford Algorithm** (Shortest Path with Negative Weights)
    * *Financial Arbitrage:* Finding a sequence of currency trades (the "path") that results in a profit, which is only possible with a negative cycle.
* **Traveling Salesperson Problem (TSP) Approximation Heuristics** (e.g., Nearest Neighbor)
    * *Drilling Paths:* Optimizing the path a drill head takes to bore a set of holes on a circuit board to minimize time.
* **Edit Distance / Levenshtein Distance** (Dynamic Programming)
    * *DNA Sequence Alignment:* Measuring the similarity between two strands of DNA by counting the minimum number of insertions, deletions, or substitutions required to change one into the other.

## String and Text Processing

* **KMP (Knuth-Morris-Pratt)** (String Searching)
    * *Malware Detection:* Efficiently searching through a large file or memory for a specific, known byte pattern (the "signature").
* **Rabin-Karp Algorithm** (String Searching/Hashing)
    * *Plagiarism Detection (Alternative to simple hashing):* Used for comparing substrings efficiently, often in systems that require rolling hashes.
* **Regular Expressions (Regex) Engines** (State Machines)
    * *Input Validation:* Ensuring a user-entered email address or phone number matches a specific, required format.

## Numerical and Scientific Computing

* **Euclidean Algorithm** (Greatest Common Divisor)
    * *Cryptography (RSA):* A fundamental step in finding the modular inverse when generating the private key for the RSA algorithm.
* **Fast Fourier Transform (FFT)**
    * *Audio Equalization/Filtering:* Decomposing an audio signal (or any wave) into its component frequencies, allowing for selective boosting or removal of bass, treble, etc.
* **Monte Carlo Methods** (Simulation)
    * *Risk Assessment:* Estimating the probability of success for a project (e.g., building a bridge) by running thousands of random simulations.
*  **Sieve of Eratosthenes** (Prime number generation)

## Hashing and Cryptography

* **Hash Tables**
    * *Password Manager:* Storing and retrieving credentials using keys for fast access.
    * *Spam Filter:* Counting word frequencies for classification.
    * *Cache Simulation:* Implementing an LRU (Least Recently Used) cache.
* **Hashing Algorithms**
    * *Password Storage System:* Using SHA-256 (with salting) to securely store credentials.
    * *File Integrity Checker:* Generating MD5/SHA checksums to verify file contents haven't changed.
    * *Plagiarism Detector:* Comparing document hashes to find similarities.
* **Cryptographic Algorithms**
    * *Caesar/Vigenère Cipher Tool:* Demonstrating basic encryption and decryption principles.
    * *RSA Key Generator:* Showing the creation of a simple public/private key pair.
    * *Secure Chat App:* Simulating end-to-end encryption.

## Compression

* **Huffman Encoding**
    * *Text File Compressor:* Demonstrating lossless data compression.
    * *Image Compression (Simplified):* Encoding pixel data based on frequency.
    * *Encrypted Messaging App:* Combining data compression with cryptography.

## Machine Learning and Data Science

* **Q-Learning** (Reinforcement Learning)
    * *Tic-Tac-Toe AI:* Training an agent to learn optimal moves through trial and error.
    * *Maze Navigator Bot:* Training a bot to find the exit of a maze based on rewards.
    * *Simple Stock Trading Bot:* Making reward-based decisions on buying or selling assets.

* **Linear Regression**
    * *House Price Predictor:* Estimating house prices based on features like size and location.
    * *Exam Score Estimator:* Modeling the relationship between hours studied and exam grades.
    * *Sports Performance Analyzer:* Analyzing training metrics versus results.

* **Classification Algorithms**
    * *Spam Email Classifier (Naive Bayes):* Identifying emails as spam or not spam.
    * *Iris Flower Species Predictor (k-NN):* Classifying objects based on feature similarity to neighbors.
    * *Sentiment Analysis Tool:* Determining if reviews are positive, negative, or neutral.

* **Clustering Algorithms**
    * *Customer Segmentation:* Grouping customers by purchase behavior for targeted marketing.
    * *Image Color Quantization:* Reducing the number of colors in an image while minimizing visual loss.
    * *Anomaly Detection in Data:* Identifying outliers in a dataset (e.g., fraudulent transactions).

* **Association Rule (Apriori)**
    * *Market Basket Analysis:* Finding items frequently purchased together (e.g., "People who buy bread also buy butter").
    * *Movie Recommendation System:* Suggesting movies based on item sets (what other users watched).

* **Genetic Algorithms**
    * *Traveling Salesman Solver:* Optimizing routes by simulating natural selection.
    * *Timetable Generator:* Scheduling classes or meetings to avoid conflicts and optimize resources.
    * *Game AI Evolution:* Optimizing game strategies over generations.

* **ANNs / CNNs** (Artificial/Convolutional Neural Networks)
    * *Handwritten Digit Recognizer (MNIST dataset):* A classic introduction to image classification.
    * *Emotion Detection from Text:* Building a simple Natural Language Processing (NLP) model.
    * *Basic Image Classifier (Cats vs. Dogs):* Distinguishing between simple image categories.

## Computer Vision

Techniques for Color channel separation, filtering (blurring, sharpening), geometric transformations (rotation, scaling), and feature detection.

* **YOLO (You Only Look Once)** (Object Detection)
    * *Real-Time Tracking:* A fast, single-pass system for simultaneously detecting and classifying multiple objects (like reading license plates in a video stream).

* **Viola-Jones Algorithm** (Face Detection)
    * *Face Detection App (Haar cascades):* Identifying the presence and location of human faces using a fast cascade of simple features.

* **AR Marker Detector** (e.g., **ArUco Markers**)
    * *Marker Recognition:* Recognizing unique square fiducial markers (like specialized QR codes) for augmented reality applications and camera pose estimation.

* **Tesseract OCR Engine** (Optical Character Recognition)
    * *Receipt Scanner:* Extracting totals and dates from images of receipts.
    * *Business Card Reader:* Parsing contact information from a photograph of a card.

* **Max-Margin Object Detector (MMOD) CNN**, *Detection for varying head poses*.
    This deep learning approach uses a Convolutional Neural Network (CNN) to achieve high accuracy and robustness, especially for faces at odd angles, under occlusion, or in low-light conditions.

* **Histogram of Oriented Gradients (HOG) + Linear SVM**, *Fast frontal face detection*.
    This classic method uses Histogram of Oriented Gradients (HOG) as a feature descriptor, which is then fed into a Linear Support Vector Machine (SVM) to classify and locate frontal or near-frontal faces. It is computationally efficient and fast on a CPU.

* **Ensemble of Regression Trees (Shape Predictor)**, *Facial landmark location and face alignment*.
    This algorithm is used to locate precise facial landmarks (like the corners of the eyes and nose) on a detected face. The coordinates of these landmarks are then used to geometrically transform and align the face to a standard orientation and size, which is critical for recognition accuracy.

## Networking

* **TCP Handshake / Sliding Window Protocol**
    * *Chat Application (TCP sockets):* Demonstrating the reliable, connection-oriented communication process, including connection setup and flow control.

* **Distributed Hash Table (DHT)** (e.g., **Kademlia**)
    * *P2P File Sharing Simulator:* Modeling distributed hash tables for decentralized file lookup and routing in peer-to-peer systems.

* **Bilateral Filter**
    * *Image Denoising:* Applying a non-linear filter to images to reduce noise while preserving edges (a common preprocessing step in vision pipelines).

* **Packet Sniffer** (e.g., **ARP Protocol / Wireshark Techniques**)
    * *Network Traffic Analysis:* Analyzing network traffic and protocols, which involves understanding protocols like ARP for mapping IP to MAC addresses.

* **Checksum Algorithm (e.g., Internet Checksum)**
    * *IP and UDP Header Validation:* A simple, fast checksum algorithm used by protocols like IP and UDP to verify the integrity of the header of every packet transmitted across the internet.

* **Diffie-Hellman Key Exchange**
    * *Secure Communication Setup:* A fundamental protocol allowing two parties to establish a shared, secret cryptographic key over an unsecured public channel, which is the basis for many secure communication systems (SSL/TLS).

* **Digital Signature Algorithm (DSA) / RSA Signatures**
    * *Software/Document Verification:* Algorithms that allow a party to mathematically "sign" a digital document (like a software executable or a certificate) to prove its authenticity and ensure it hasn't been tampered with since being signed.

## Memory Management

* **Bloom Filter**
    * *Database Query Optimization:* Quickly checking if a username or element *might* be in a large database *before* doing an expensive disk lookup (allows false positives, but no false negatives).
* **Garbage Collection** (e.g., Mark-and-Sweep)
    * *Memory Management:* Automatically reclaiming memory used by objects that are no longer being referenced in a programming language like Java or Python.

### Advanced Sampling and Data Processing

* **Reservoir Sampling**
    * *Big Data Stream Analysis:* Selecting a uniform random sample of size $k$ from a large data stream of unknown length $n$ (where $n$ is too big to fit in memory), commonly used for sampling social media feeds or search queries.
* **Linear Congruential Generator (LCG)**
    * *Simple Random Number Generation:* A simple and fast algorithm for generating sequences of pseudorandom numbers, often used in older simulations or basic programming exercises.
* **Fisher-Yates (Knuth) Shuffle**
    * *Randomization in Games/Tests:* Generating a perfectly uniform random permutation of a finite set (e.g., shuffling a deck of cards or randomizing test questions).
* **Reed-Solomon Error Correction**
    * *QR Code Generation/Reading:* The core mathematical algorithm used to encode redundancy into QR codes (and CDs, DVDs) so that they can be correctly read even if a large portion is damaged, dirty, or obscured.

### Scientific Computing and Graphics

* **Bresenham's Line Algorithm**
    * *Computer Graphics Rendering:* Drawing a straight line segment on a discrete pixel grid using only integer arithmetic (no floating-point operations), which was crucial for early and fast graphics hardware.
* **Perlin Noise**
    * *Procedural Content Generation:* Creating realistic, natural-looking textures, terrains, and fire/smoke effects in video games and visual effects by generating coherent, gradient-based random values.
* **Ray Tracing (The Basic Algorithm)**
    * *Realistic Rendering:* Simulating realistic lighting and reflections by tracing the path of light rays backward from the viewer's eye through a pixel and into the 3D scene.
* **Graham Scan Convex Hull Algorithm**
    * Given a set of points in a 2D plane, compute the convex hull: the smallest convex polygon that contains all points.

### Distributed Systems and Concurrency

* **Two-Phase Commit (2PC)**
    * *Distributed Database Transactions:* A crucial protocol ensuring that a transaction across multiple separate databases either succeeds completely on all servers or fails completely on all of them ("all or nothing").
* **Paxos / Raft** (Consensus Algorithms)
    * *Fault-Tolerant Distributed Storage:* Algorithms used to achieve agreement (consensus) among a group of servers, even if some servers fail, forming the backbone of highly-available systems like Google File System or etcd.


---

(I acknowledge the use of various LLMs to help curate parts of this list)


