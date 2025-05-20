# LaTeX Code Sheet for Math Equations in PostgreSQL

## Purpose

This document provides guidelines and examples for inserting LaTeX-formatted math into the text field of a  PostgreSQL database. It provides a table LaTeX codes (beginning with a backslash "\") and addresses formatting and escaping for complex math expressions.



## Sample Log into PostgreSQL on Heroku:

First, log into the Heroku PostgreSQL database:

```sql
heroku pg:psql -a my-physics-formula-viewer-3x
```

Then, turn off the *pager* setting:

```sql
\pset pager off
```



## Common LaTeX Syntax in Physics & Math

| Concept          | LaTeX Code                                                   |
| ---------------- | ------------------------------------------------------------ |
| Greek Letters    | `\alpha, \beta, \epsilon, \gamma, \mu, \Omega`               |
| Superscripts     | `x^2, e^{i\pi}`                                              |
| Subscripts       | `a_1, V_{max}`                                               |
| Fractions        | `\frac{a}{b}`                                                |
| Roots            | `\sqrt{x}, \sqrt[n]{x}`                                      |
| Derivatives      | `\frac{dy}{dx}, \partial`                                    |
| Vectors/Matrices | `\vec{v}, \mathbf{F}, \begin{bmatrix} a & b \\ c & d \end{bmatrix}` |
| Integrals        | `\int_a^b f(x) \, dx`                                        |
| Summations       | `\sum_{i=1}^n i^2`                                           |
| Limits           | `\lim_{x \to \infty}`                                        |



## Sample INSERT Query:

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  'Random Variable (Statistics)',
  'X = \mu + \epsilon',
  25,
  'This is the general formula for a random variable X in statistics. μ represents the constant factor. ϵ represents the random disturbance.'
);
```



## Sample UPDATE Query:

```sql
UPDATE formula
SET latex = 'X = \mu + \epsilon'
WHERE id = 101;
```



## Basic Formatting Rules:

### SQL String Handling

- **Use single quotes** for SQL string literals.

- **Escape internal single quotes** by *doubling* them:
  
  - `'Newton''s Law'` ← Correct
  
- **Backslashes (`\`) should be written normally in your SQL string**—PostgreSQL will preserve them when storing the LaTeX:

  - `'\alpha'` remains `\alpha` in the database

    

## Simple LaTeX Formula Examples

| Formula Name        | LaTeX Code                               | Notes                                 |
| ------------------- | ---------------------------------------- | ------------------------------------- |
| Newton's 2nd Law    | `F = ma`                                 | No escaping required                  |
| Pythagorean Theorem | `a^2 + b^2 = c^2`                        | Use `^` for powers                    |
| Quadratic Formula   | `x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}` | Requires escaping `\frac` and `\sqrt` |



## Complex LaTeX Formula Examples

### Example: Schrödinger Equation

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  'Schrödinger Equation',
  'i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H\Psi(\mathbf{r},t)',
  10,
  'Describes time evolution of quantum state.'
);
```

### Example: Maxwell’s Equations

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  'Maxwell Gauss Law',
  '\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}',
  20,
  'Gauss’s law for electricity: Electric flux relates to charge density.'
);
```



## Escaping Tips

| LaTeX Character  | Use in SQL as... | Example                |
| ---------------- | ---------------- | ---------------------- |
| `\` (backslash)  | As-is (`\`)      | `'\alpha + \beta'`     |
| `'` (apostrophe) | Double it (`''`) | `'Euler''s Identity'`  |
| `%`              | OK as-is         | `'x \% y'` (if needed) |



## Helper SQL Template

```sql
INSERT INTO formula (formula_name, latex, display_order, formula_description)
VALUES (
  '<Formula Title>',
  '<Escaped LaTeX Code>',
  <display_order>,
  '<Short Description>'
);
```



## Optional: Storing MathJax-Compatible Code

If you use MathJax for rendering, your stored LaTeX will be wrapped by delimiters in the frontend (e.g., `\( \)` for inline or `\[ \]` for block math), **not in the DB**.

---
