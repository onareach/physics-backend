# Heroku API Documentation

## Overview

This document describes the API endpoints provided by the Physics Formula Viewer backend hosted on Heroku. The backend has been converted from a Flask web application with templates to a pure API that serves the Next.js frontend.

## API Base URL

```
https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com
```

## Endpoints

### 1. Get All Formulas

**Endpoint:** `/api/formulas`

**Method:** GET

**Description:** Retrieves all physics formulas from the database, ordered by display_order.

**Response Format:**
```json
[
  {
    "id": 1,
    "formula_name": "Newton's Second Law",
    "latex": "F = ma",
    "display_order": 1,
    "formula_description": "Newton's Second Law states that the force (F) acting on an object is equal to the mass (m) of the object multiplied by its acceleration (a)."
  },
  {
    "id": 2,
    "formula_name": "Einstein's Mass-Energy Equivalence",
    "latex": "E = mc^2",
    "display_order": 2,
    "formula_description": "Einstein's famous equation relating energy (E) to mass (m) and the speed of light (c)."
  }
  // ... more formulas
]
```

### 2. Get Formula by ID

**Endpoint:** `/api/formulas/{id}`

**Method:** GET

**Description:** Retrieves a specific formula by its ID.

**Parameters:**
- `id` (path parameter): The ID of the formula to retrieve

**Response Format:**
```json
{
  "id": 1,
  "formula_name": "Newton's Second Law",
  "latex": "F = ma",
  "display_order": 1,
  "formula_description": "Newton's Second Law states that the force (F) acting on an object is equal to the mass (m) of the object multiplied by its acceleration (a)."
}
```

**Error Response:**
```json
{
  "error": "Formula not found"
}
```

## CORS Configuration

The API is configured to allow requests from the following origins:
- `http://localhost:3000` (for local development)
- `https://physicswebprod.vercel.app` (for the production frontend)

## Implementation Notes

- The API uses direct PostgreSQL connections via psycopg2 instead of SQLAlchemy ORM
- The templates folder and index.html template are no longer required as the frontend is now separate
- Error handling is implemented for all endpoints
- The API returns JSON responses for all endpoints

## Usage Example

Using fetch in JavaScript:

```javascript
// Fetch all formulas
fetch('https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com/api/formulas')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// Fetch a specific formula
fetch('https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com/api/formulas/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```
