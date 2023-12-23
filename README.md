# Auto Test
## Purpose
The purpose of this project is creating a generalized, hopefully more simplistic way of handling test cases for problems.
Ideally, this is going to be used in any problem available made with a coding language.
## Terminology
- BNF: [Backus-Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
- Jerry _plural: Jerri_: [Equivalence Class](https://en.wikipedia.org/wiki/Equivalence_partitioning)
## Implementation
This program is going to create a series of txt files, having test cases from problems all over the coding world.
These test cases are going to be random values made from Jerri that are researched from the question handler.
Such Jerri are written in an original file called case_gen.txt in a certain structure, which is read from a program called case_parser.py.
This file will parse each argument and the final mashup and with each condition given, will give each argument to case_gen.py, which will generate each test case in their own.
Since to create an output you need to create a base program first, you can create that and run each test case on output_case.py and it will create a file series just as long, with output test cases.
This way, you do not need to create test cases for it, but simply researching which Jerry do you need, which is exhaustive and may prove wrong due to human error.
However, the only exhaustive part (less so) is research on what Jerry works and what doesn't.

Research about the question consists of:
1. Finding the question to be used in Auto Test
2. Finding its required inputs in its data types
3. Finding Jerri for each argument that may or may not be used
4. Collecting each Jerry in the mashup to describe which may be right to make test cases with or not
5. Write them in case_gen.txt
## Versions
### 1
This version will potentially handle simple, primitive data types and generate from them.
This should work for any procedurial paradigm problem (e.g C)
#### 1.0
- Is draft
- Does not exist as code, but as a BNF
- BNF is in its branch
#### 1.1
- First code of the repo
- BNF is updated to include Jerry Mashup
- Added double as data type (dubbed **dub**)
- Removed char data type (int in disguise)
- Removed bool data type (int in disguise)
