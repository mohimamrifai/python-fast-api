# FastAPI CRUD API Example

This is a simple CRUD (Create, Read, Update, Delete) API built with FastAPI framework.

## Features

- Basic CRUD operations for items
- Bulk create items
- Custom JSON response format
- Input validation using Pydantic models

## API Endpoints

### Root
- `GET /` - Root endpoint that returns "Hello World"

### Items
- `GET /items/` - Get all items
- `POST /items/` - Create a single item
- `POST /items/bulk` - Create multiple items
- `GET /items/{item_id}` - Get specific item by ID
- `PUT /items/{item_id}` - Update item by ID
- `DELETE /items/{item_id}` - Delete item by ID

### Auth
- `POST /auth/login` - Login
- `POST /auth/register` - Register
