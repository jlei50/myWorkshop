from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'story.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                latest_update TEXT,
                creator_id INTEGER,
                FOREIGN KEY(creator_id) REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS contributions (
                user_id INTEGER,
                story_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(story_id) REFERENCES stories(id)
            );
        ''')
        db.commit()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = query_db('SELECT * FROM users WHERE username = ? AND password = ?', [username, password], one=True)
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, password])
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    my_stories = query_db('SELECT * FROM stories WHERE creator_id = ?', [user_id])
    other_stories = query_db('SELECT * FROM stories WHERE creator_id != ?', [user_id])
    return render_template('home.html', my_stories=my_stories, other_stories=other_stories)

@app.route('/create', methods=['GET', 'POST'])
def create_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        db = get_db()
        db.execute('INSERT INTO stories (title, latest_update, creator_id) VALUES (?, ?, ?)', [title, '', session['user_id']])
        db.commit()
        return redirect(url_for('home'))
    return render_template('create_story.html')

@app.route('/edit/<int:story_id>', methods=['GET', 'POST'])
def edit_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form['content']
        db = get_db()
        db.execute('UPDATE stories SET latest_update = ? WHERE id = ?', [content, story_id])
        db.execute('INSERT INTO contributions (user_id, story_id) VALUES (?, ?)', [session['user_id'], story_id])
        db.commit()
        return redirect(url_for('home'))
    story = query_db('SELECT * FROM stories WHERE id = ?', [story_id], one=True)
    return render_template('edit_story.html', story=story)

@app.route('/view/<int:story_id>')
def view_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    story = query_db('SELECT * FROM stories WHERE id = ?', [story_id], one=True)
    return render_template('view_story.html', story=story)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return (rv[0] if rv else None) if one else rv

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
