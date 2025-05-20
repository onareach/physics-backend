# 📘 Guide: Inserting and Updating LaTeX Formulas in PostgreSQL for MathJax Rendering

This guide explains how to correctly insert and update LaTeX formulas in the Heroku-hosted PostgreSQL database used by the Physics Formula Viewer app. The frontend uses MathJax to render formulas, so the LaTeX strings must be stored in the correct format.

---

## 🔐 Step 1: Log into the Heroku Database

In the terminal:

```bash
heroku pg:psql -a my-physics-formula-viewer-3x
```

This command connects you to the PostgreSQL database hosted on Heroku.

## 📋 Step 2: View Existing Formulas

To see all formulas currently in the database:

```sql
SELECT * FROM formula ORDER BY display_order;
```

## ➕ Step 3: Insert a New Formula

To add a new formula to the database:

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  'Newton''s Second Law',
  'F = ma',
  1,
  'Newton''s Second Law states that the force (F) acting on an object is equal to the mass (m) of the object multiplied by its acceleration (a).'
);
```

### Important Notes on LaTeX Formatting:

- For simple formulas like `F = ma`, you can enter them directly
- For complex formulas with special LaTeX symbols, ensure proper escaping:
  - Use single quotes for SQL strings
  - Double any single quotes within the string (e.g., `'Newton''s Law'`)
  - For LaTeX commands, use the backslash as normal (e.g., `'\frac{1}{2}'`)

### Example with Complex LaTeX:

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  'Schrödinger Equation',
  'i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H\Psi(\mathbf{r},t)',
  10,
  'The Schrödinger equation describes how the quantum state of a physical system changes over time.'
);
```

## 🔄 Step 4: Update an Existing Formula

To update an existing formula:

```sql
UPDATE formula
SET 
  formula_name = 'Updated Name',
  latex = 'E = mc^2',
  formula_description = 'Updated description of the formula.'
WHERE id = 1;
```

## 🗑️ Step 5: Delete a Formula

To remove a formula from the database:

```sql
DELETE FROM formula WHERE id = 3;
```

## 🔢 Step 6: Reorder Formulas

To change the display order of formulas:

```sql
UPDATE formula SET display_order = 5 WHERE id = 2;
```

After reordering, you may want to normalize the display_order values:

```sql
-- First, create a temporary sequence
WITH ordered_formulas AS (
  SELECT id, ROW_NUMBER() OVER (ORDER BY display_order) AS new_order
  FROM formula
)
-- Then update all formulas with the new sequence
UPDATE formula
SET display_order = o.new_order
FROM ordered_formulas o
WHERE formula.id = o.id;
```

## 📊 Step 7: Verify Your Changes

After making changes, verify them with:

```sql
SELECT id, formula_name, latex, display_order, formula_description 
FROM formula 
ORDER BY display_order;
```

## 🔍 Tips for Testing LaTeX Rendering

1. You can test your LaTeX syntax on websites like [LaTeX Equation Editor](https://www.latexedit.com/) before adding it to the database
2. Remember that the frontend uses MathJax to render the formulas, so the syntax should be compatible
3. For complex formulas, consider breaking them into smaller parts or adding line breaks for better display on mobile devices

## 📱 Viewing Changes on the Frontend

After updating the database, visit the frontend application to see your changes:
[https://physicswebprod.vercel.app](https://physicswebprod.vercel.app)

Changes should be visible immediately as the frontend fetches data directly from the API.
