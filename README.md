# Physics Formula Viewer Backend API

## Overview

This is the backend API for the Physics Formula Viewer application. It provides RESTful endpoints to access physics formulas stored in a PostgreSQL database.

Originally part of a monorepo, this backend is now managed as a standalone GitHub repository.

- **Framework:** Flask (Python)
- **Database:** PostgreSQL on Heroku
- **Frontend:** See [physics-frontend](https://github.com/onareach/physics-frontend) (deployed at [physicswebprod.vercel.app](https://physicswebprod.vercel.app))
- **API Base URL:** https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com

## API Endpoints

- `GET /api/formulas`: Fetch all formulas
- `GET /api/formulas/{id}`: Fetch a specific formula by ID

## Project Structure

```
physics-backend/
├── app.py                      # Main API application
├── models.py                   # Database models
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku deployment configuration
├── Heroku_API_README.md       # API documentation
├── Adding_Formulas_to_the_Database.md
├── templates/                 # (optional legacy remnants)
├── LICENSE
├── README.md
```

## Local Development Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv_physics_backend
source venv_physics_backend/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
export DATABASE_URL=your_postgresql_database_url
```

4. Run the development server:

```bash
flask run
```

## Deployment to Heroku

1. Create a Heroku app:

```bash
heroku create my-physics-formula-viewer-3x
```

2. Add PostgreSQL addon:

```bash
heroku addons:create heroku-postgresql --app my-physics-formula-viewer-3x
```

3. Deploy to Heroku:

```bash
git push heroku main
```

4. Initialize the database:

```bash
heroku run python
```

Then in the shell:

```python
from app import app, db
with app.app_context():
    db.create_all()
```

## Database Schema

```python
class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(100), nullable=False)
    latex = db.Column(db.Text, nullable=False)
    display_order = db.Column(db.Integer)
    formula_description = db.Column(db.Text)
```

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-CORS
- psycopg2-binary
- gunicorn

## Adding Formulas

See `Adding_Formulas_to_the_Database.md` for detailed instructions.

## License

MIT License. See `LICENSE` file.