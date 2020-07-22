from flask import Flask, render_template, request, redirect, g
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure Database Connection
def get_db():
    db = sqlite3.connect('database.db')
    # makes sure queries are returned as dictionaries
    db.row_factory = sqlite3.Row
    return db


# combines getting the cursor, executing and fetching the results
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# insertion query
def insert_db(query, args):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    db.commit()
    db.close()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():
    users = query_db('SELECT * FROM experts')
    return render_template('index.html', users=users)


@app.route('/about')
def about():
    # Open about page
    return render_template('about.html')


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        # Open Quiz
        return render_template('quiz.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        curl = request.form.get('curlpattern')
        length = request.form.get('length')
        density = request.form.get('density')
        porosity = request.form.get('porosity')
        oily = request.form.get('oily')
        colored = request.form.get('colored')
        permed = request.form.get('permed')
        keratin = request.form.get('keratin')
        washMethod = request.form.get('washMethod')

        insert_db("""INSERT INTO experts (name, email, curl,length, density,
        porosity, oily, colored, permed, keratin, washMethod)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, email, curl, length, density, porosity, oily, colored, permed, keratin, washMethod))

        return redirect('/results')


@ app.route('/results')
def results():
    user = query_db('select * from experts ORDER BY id DESC')
    user = user[0]
    methods = query_db('select * from experts where curl = ? and length = ? and density = ? and porosity=? and oily = ? and colored = ? and permed = ? and keratin =?',
                       (user["curl"], user["length"], user["density"], user["porosity"], user["oily"], user["colored"], user["permed"], user["keratin"]))
    matches = len(methods)
    return render_template('results.html', count=matches, methods=methods)
