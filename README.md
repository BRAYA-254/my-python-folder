# Python Learning Repository

This repository contains my Python learning exercises and examples. It documents my progress in learning Python programming, starting with basic programming concepts, operators, and arrays using NumPy.

## Topics Covered

### 1. Python Basics

This section introduces the fundamental concepts of Python programming.

Topics covered:

* Printing output using `print()`
* Variables
* Python data types

  * Strings
  * Integers
  * Floats
  * Booleans
* Formatted strings (f-strings)
* User input using `input()`
* Basic arithmetic calculations

### 2. Python Operators

This section covers different types of operators used in Python to perform calculations, compare values, combine conditions, update variables, and work with objects and collections.

#### Arithmetic Operators

Used to perform mathematical operations.

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Floor Division `//`
* Modulus `%`
* Exponentiation `**`

#### Comparison Operators

Used to compare values and return either `True` or `False`.

* Equal to `==`
* Not equal to `!=`
* Greater than `>`
* Less than `<`
* Greater than or equal to `>=`
* Less than or equal to `<=`

#### Logical Operators

Used to combine or modify conditions.

* `and`
* `or`
* `not`

#### Assignment Operators

Used to assign and update values stored in variables.

* `=`
* `+=`
* `*=`

#### Membership Operators

Used to check whether a value exists in a sequence such as a list.

* `in`
* `not in`

#### Identity Operators

Used to check whether two variables refer to the same object.

* `is`
* `is not`

### 3. NumPy Arrays

This section introduces arrays using the **NumPy** library.

Topics covered:

* Importing NumPy
* Creating one-dimensional (1D) arrays
* Creating two-dimensional (2D) arrays
* Introduction to multidimensional arrays
* Performing arithmetic operations on arrays
* `np.arange()`
* `np.zeros()`
* `np.ones()`
* Generating random numbers with `np.random.rand()`
* Generating random integers with `np.random.randint()`

#### One-Dimensional Arrays

Example:

```python
import numpy as np

n = np.array([10, 20, 30])
print(n)
```

#### Two-Dimensional Arrays

Example:

```python
n1 = np.array([[10, 20, 30], [40, 50, 60]])
print(n1)
```

#### Creating Arrays with NumPy Functions

Examples include:

```python
np.arange(4)
np.zeros((2, 3))
np.ones((2, 3))
np.random.rand(5)
np.random.rand(2, 3)
np.random.randint(1, 10, 5)
```

## Repository Structure

```text
Python-Learning/
│
├── basics.py
├── operators.py
├── arrays.py
└── README.md
```

## Purpose

The purpose of this repository is to practice Python programming concepts through simple examples and exercises. It serves as a record of my progress as I continue learning Python.

## Technologies Used

* Python
* NumPy

## Learning Progress

* [x] Python Basics
* [x] Python Operators
* [x] NumPy Arrays
* [ ] Conditional Statements
* [ ] Loops
* [ ] Functions
* [ ] More Python Concepts

## Author

**Brighton Okhalo**
