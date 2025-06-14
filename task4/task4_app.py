from flask import Flask, render_template, request

app = Flask(__name__)

# Root URL renders the form
@app.route('/', methods=['GET'])
def index():
    return render_template('nth_largest.html')

@app.route('/nth_largest', methods=['GET', 'POST'])
def nth_largest():
    nth_largest = None
    error = None
    if request.method == 'POST':
        try:
            # Get numbers from form and convert them into a list of integers
            numbers = list(map(int, request.form['numbers'].split(',')))
            n = int(request.form['n'])
            
            # Check if n is within bounds of the list
            if n > len(numbers) or n <= 0:
                error = "Error: n is greater than the length of the list or less than 1."
                nth_largest = None
            else:
                # Sort numbers in descending order
                sorted_numbers = sorted(numbers, reverse=True)
                nth_largest = sorted_numbers[n - 1]
        
        except ValueError:
            error = "Invalid input. Please make sure the input is in the correct format."
            nth_largest = None

    return render_template('nth_largest.html', nth_largest=nth_largest, error=error)

if __name__ == '__main__':
    app.run(debug=True)
