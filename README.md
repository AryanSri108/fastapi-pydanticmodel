# FastAPI with SQLite, SQLAlchemy, and Pydantic

This project is a FastAPI application with SQLite as the database and SQLAlchemy as the ORM. It includes Pydantic for request and response validation and demonstrates basic CRUD operations on a `User` table.

## Features
- **FastAPI**: A modern web framework for quickly building APIs.
- **SQLAlchemy**: ORM for database interactions with SQLite.
- **Pydantic**: Data validation and parsing using Python type annotations.
- **SQLite**: Lightweight database for easy development and testing.

## Prerequisites
- Python 3.12.6

## Project Setup

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/AryanSri108/fastapi-pydanticmodel.git
cd fastapi-pydanticmodel

### 2. Install the required packages by running
pip install fastapi uvicorn sqlalchemy pydantic

### 3. Run the Application
uvicorn main:app --reload
