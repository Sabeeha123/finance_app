from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"   # for session

# ---------------- DATABASE ---------------- #
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    # users table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
    """)

    # transactions table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            type TEXT,
            category TEXT,
            date TEXT,
            notes TEXT
        )
    """)

    # default users
    conn.execute("INSERT OR IGNORE INTO users VALUES (1,'admin','admin123','admin')")
    conn.execute("INSERT OR IGNORE INTO users VALUES (2,'viewer','viewer123','viewer')")

    conn.commit()
    conn.close()

init_db()

# ---------------- LOGIN ---------------- #
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect("/dashboard")
        else:
            return "Invalid credentials!"

    return render_template("login.html")

# ---------------- LOGOUT ---------------- #
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- DASHBOARD ---------------- #
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    transactions = conn.execute("SELECT * FROM transactions").fetchall()

    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense

    return render_template("index.html",
                           transactions=transactions,
                           income=income,
                           expense=expense,
                           balance=balance,
                           role=session["role"])

# ---------------- ADD ---------------- #
@app.route("/add", methods=["GET", "POST"])
def add():
    if session.get("role") != "admin":
        return "Access Denied!"

    if request.method == "POST":
        conn = get_db()
        conn.execute(
            "INSERT INTO transactions VALUES (NULL,?,?,?,?,?)",
            (
                request.form["amount"],
                request.form["type"],
                request.form["category"],
                request.form["date"],
                request.form["notes"]
            )
        )
        conn.commit()
        return redirect("/dashboard")

    return render_template("add.html")

# ---------------- EDIT ---------------- #
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if session.get("role") != "admin":
        return "Access Denied!"

    conn = get_db()

    if request.method == "POST":
        conn.execute("""
            UPDATE transactions
            SET amount=?, type=?, category=?, date=?, notes=?
            WHERE id=?
        """, (
            request.form["amount"],
            request.form["type"],
            request.form["category"],
            request.form["date"],
            request.form["notes"],
            id
        ))
        conn.commit()
        return redirect("/dashboard")

    transaction = conn.execute("SELECT * FROM transactions WHERE id=?", (id,)).fetchone()
    return render_template("edit.html", transaction=transaction)

# ---------------- DELETE ---------------- #
@app.route("/delete/<int:id>")
def delete(id):
    if session.get("role") != "admin":
        return "Access Denied!"

    conn = get_db()
    conn.execute("DELETE FROM transactions WHERE id=?", (id,))
    conn.commit()
    return redirect("/dashboard")

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(debug=True)