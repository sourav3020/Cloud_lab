from flask import Flask, render_template, request

app = Flask(__name__)

# Root URL renders the form
@app.route('/', methods=['GET'])
def index():
    return render_template('task3_validate_user.html')

# Handles form submission and just validates success
@app.route('/validate_user', methods=['POST'])
def validate_user():
    # Get username and password from the form (although we aren't checking them)
    username = request.form['username']
    password = request.form['password']
    
    # Simply return "Validation successful" without checking with the database
    return 'Validation successful'

if __name__ == '__main__':
    app.run(debug=True)
