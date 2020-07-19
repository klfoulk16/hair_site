from flask import Flask, render_template, request, redirect
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure Database Connection


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM experts').fetchall()
    conn.close()
    return render_template('index.html', users=users)


@app.route('/about')
def about():
    # Open about page
    return render_template('about.html')


@app.route('/name', methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        # Open Quiz
        return render_template('name.html')
    else:
        name = request.form.get('name')
        hairtype = request.form.get('hairtype')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO experts (name, curl) VALUES (?, ?)",
                    (name, hairtype)
                    )
        conn.commit()
        conn.close()

        return redirect('/results')


@app.route('/results')
def results():
    return render_template('results.html')
