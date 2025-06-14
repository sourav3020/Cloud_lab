from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host='dpg-d0pj1qodl3ps73argvhg-a',
        database='cloud_lab_8br0',
        user='cloud_lab_8br0_user',
        password='McBRr8DyPse7bAX7B3bzBTbWaoXNtOnt'
    )
    return conn

# Root URL renders the form
@app.route('/', methods=['GET'])
def index():
    return render_template('task3_validate_user.html')

# Handles form submission
@app.route('/validate_user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']

    # Check if the user exists in the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Query to check if the user exists
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        return 'User validated successfully.'
    else:
        return 'Invalid username or password.'

if __name__ == '__main__':
    app.run(debug=True)
