# SieveOfEratosthenes-Manim

This repository contains an animation of the **Sieve of Eratosthenes** algorithm, created using **Manim**. The animation visually demonstrates how the algorithm efficiently finds prime numbers by marking non-prime multiples.

## Overview

The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to a given limit `n`. The algorithm works by iteratively marking the multiples of each prime starting from 2. 

I was fascinated by how the Sieve of Eratosthenes can generate primes in **O(n log log n)** time. To better understand the concept and practice with Manim, I created an animation to visualize how the sieve operates.

## Tools Used

- **Manim Community Edition (CE)**: A Python library for mathematical animations.
- **Online Manim Jupyter Notebook**: The animation was created using the Manim Jupyter notebook available on the Manim Community Edition website.

## Features

- Visual representation of the Sieve of Eratosthenes algorithm.
- Marking of prime numbers in distinct colors.
- Highlighting of multiples as they are crossed out.
- Final marking of the prime numbers in bold and distinct color.

## Installation

If you want to run the code on your local machine, you'll need to install **Manim**. Follow these steps to set up Manim on your system:

1. **Install Manim**:
   ```bash
   pip install manim
Clone this repository:

bash
Copy
git clone https://github.com/Ayaan-Khan-079/SieveOfEratosthenes-Manim.git
Run the animation: Navigate to the folder where the project is stored, then run:

bash
Copy
manim -pql sieve_of_eratosthenes.py
How to Run the Animation
The animation was originally created and run on the Manim Jupyter notebook available on the Manim Community Edition website. However, you can also run the provided script locally by installing Manim on your machine.

Notes
This is a simple animation, but I learned a lot while making it work.
Feel free to modify the code and experiment with different algorithms or animations using Manim.
