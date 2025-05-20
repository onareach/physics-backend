# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(100), nullable=False)
    latex = db.Column(db.Text, nullable=False)
    display_order = db.Column(db.Integer)
    formula_description = db.Column(db.Text)

    def __repr__(self):
        return f"<Formula {self.formula_name}>"
