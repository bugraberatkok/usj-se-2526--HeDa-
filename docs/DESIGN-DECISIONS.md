# Design Decisions

## 1. Tech stack overview

We were already decided to implement our backend in **Python** at the beginning of the semester.  
For the HTTP framework, we chose **Flask**.  
For testing, we chose **pytest**.

Our goal is to use simple but strong tools so that we can focus on our domain model and good code quality.

---

## 2. HTTP framework: Flask

Flask is a small and lightweight web framework for Python.  
It helps us create HTTP endpoints in a simple way.

We chose Flask for these reasons:

- It is easy to learn and understand.
- It is very popular in the Python community.
- The documentation is clear and has many examples.
- We already know some basic Python, so it is a natural choice.

With Flask, we can quickly create routes like `GET /items` or `GET /users` and return JSON responses.

---

## 3. Testing framework: pytest

pytest is a testing framework for Python.  
It helps us write and run unit tests for our domain models.

We chose pytest for these reasons:

- The syntax is simple and readable.
- It is one of the most popular testing tools in Python.
- It is easy to test invalid constructions and invariants in our value objects.
- It gives clear error messages when a test fails.
