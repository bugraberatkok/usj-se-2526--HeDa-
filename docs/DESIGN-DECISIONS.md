# Design Decisions

## 1. Tech stack overview

We chose FastAPI for our backend because it is a modern, lightweight, and API-focused framework that fits the needs of our project. Since Heda is built around HTTP endpoints and data exchange rather than server-rendered pages, FastAPI’s design aligns naturally with our goals. Its use of Python type hints and Pydantic models gives us automatic validation and clean data structures, which helps maintain the correctness of our domain logic with less code. FastAPI also provides automatic interactive documentation through Swagger UI, making development, testing, and team collaboration easier. Additionally, its support for asynchronous execution offers high performance and leaves room for future scalability if we include features like real-time interactions.

For testing, we selected pytest because it offers a simple and readable syntax that reduces boilerplate compared to Python’s built-in unittest framework. This simplicity encourages writing more tests and makes them easier to maintain, which is important since our project requires a significant number of unit tests for domain models and invariants. pytest also integrates seamlessly with FastAPI, has excellent error messages, and includes useful tools like fixtures and plugins for testing asynchronous code. Together, FastAPI and pytest form a clean, efficient, and developer-friendly stack that allows us to build a reliable backend while keeping the codebase easy to understand and extend.

---

## 2. HTTP framework: FastAPI

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
