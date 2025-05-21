# app.py
# This app.py was created in order to expose an API endpoint for
# Vercel Next.js to call
# The Heroku API URL that this page calls is: https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com
# The Heroku PostgreSQL login is: heroku pg:psql -a my-physics-formula-viewer-3x

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)

# Below are the local host and Vercel production URL origins are permitted.
CORS(app, origins=[
    "http://localhost:3000",  # Local development
    "https://physicswebprod.vercel.app"  # Deployed Vercel site
])

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_formulas():
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute("SELECT id, formula_name, latex, display_order, formula_description FROM formula ORDER BY display_order;")
    formulas = cursor.fetchall()
    result = [{"id": row[0], "formula_name": row[1], "latex": row[2], "display_order": row[3], 
               "formula_description": row[4]} for row in formulas]
    cursor.close()
    conn.close()
    return result

# Function to fetch a single formula by ID
def get_formula_by_id(formula_id):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute("SELECT id, formula_name, latex, display_order, formula_description FROM formula WHERE id = %s;", (formula_id,))
    formula = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if formula:
        return {
            "id": formula[0],
            "formula_name": formula[1],
            "latex": formula[2],
            "display_order": formula[3],
            "formula_description": formula[4]
        }
    else:
        return None
    
# Route to fetch all formulas    
@app.route('/api/formulas', methods=['GET'])
def fetch_formulas():
    try:
        formulas = get_formulas()
        return jsonify(formulas)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch a single formula by ID
@app.route('/api/formulas/<int:formula_id>', methods=['GET'])
def fetch_formula_by_id(formula_id):
    try:
        formula = get_formula_by_id(formula_id)
        if formula:
            return jsonify(formula)
        else:
            return jsonify({"error": "Formula not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
