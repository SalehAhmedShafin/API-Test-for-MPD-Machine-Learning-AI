# Book Service

The Book Service is a FastAPI-based backend application for managing books, authors, and clients. It uses PostgreSQL for data storage and is containerized with Docker.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Configure Database URL](#2-configure-database-url)
  - [3. Build and Run the Docker Container](#3-build-and-run-the-docker-container)
  - [4. Access API Documentation](#4-access-api-documentation)
- [Testing API Endpoints](#testing-api-endpoints)
- [Stop the Docker Container](#stop-the-docker-container)
- [Security](#security)
- [More](#more)

## Prerequisites

Before running the Book Service, ensure you have the following:

1. **Docker:** [Install Docker](https://www.docker.com/get-started)
2. **Python and Pip:** [Install Python](https://www.python.org/downloads/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SalehAhmedShafin/API-Test-for-Middle-Python-Developer-Machine-Learning-AI.git
cd book_service
```

### 2. Configure Database URL
Edit the app/database.py file to set your PostgreSQL database URL:

```bash
DATABASE_URL = "postgresql://user:password@postgresserver/db"
```
Replace user, password, and postgresserver with your actual PostgreSQL database credentials and server information.

### 3. Build and Run the Docker Container
```bash
   docker build -t book-service .
   
   docker run -p 8000:80 book-service
```
### 4. Access API Documentation
   
Open your web browser and go to http://127.0.0.1:8000/docs.

This is the Swagger UI for the Book Service API, where you can interact with the API, view available endpoints, and test different requests.

### Testing API Endpoints

Use the Swagger UI or tools like curl or Postman to test the various API endpoints. Here are some example:

- Create a Book:
```bash
curl -X POST "http://127.0.0.1:8000/books/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"title": "Sample Book", "author_id": 1}'
```
- Retrieve a Book:
```bash
curl -X GET "http://127.0.0.1:8000/books/1" -H "accept: application/json"
```
- Update a Book:
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" -H "accept: application/json" -H "Content-Type: application/json" -d '{"new_title": "Updated Book", "new_author_id": 2}'
```
- Delete a Book:
```bash
curl -X DELETE "http://127.0.0.1:8000/books/1" -H "accept: application/json"
```
Repeat similar steps for other entities such as authors and clients, utilizing the provided CRUD operations.

### Stop the Docker Container

Once you are done testing, stop the Docker container:
```bash
docker stop $(docker ps -q --filter ancestor=book-service)
```
### Security
The Book Service API is secured using Bearer Token authentication.

### More
**env.py** this file:

- It imports the necessary modules and components from SQLAlchemy, Alembic, and my application (app).
- The path to the SQLAlchemy model metadata (target_metadata) is set to the Base.metadata attribute in my models module.
- The database URL is configured using the DATABASE_URL variable from app.database.
- The SQLAlchemy engine is created and attached to the Alembic config, allowing Alembic to interact with the database.

This env.py file is crucial for managing database migrations with Alembic. It is used to generate migration scripts and apply them to evolve the database schema as your application changes.
