from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nth_largest = None  # Initialize variable for the nth largest number
    error = None  # Initialize variable for errors

    if request.method == 'POST':
        try:
            # Get the numbers from the form and convert them to a list of integers
            numbers = list(map(int, request.form['numbers'].split(',')))
            n = int(request.form['n'])

            # Check if n is within the bounds of the list length
            if n > len(numbers) or n < 1:
                error = "Error: n is greater than the length of the list or less than 1."
                nth_largest = None
            else:
                # Sort the numbers in descending order to find the nth largest number
                sorted_numbers = sorted(numbers, reverse=True)
                nth_largest = sorted_numbers[n - 1]

        except Exception as e:
            error = f"Invalid input: {e}"
            nth_largest = None

    return render_template('index.html', nth_largest=nth_largest, error=error)

if __name__ == '__main__':
    app.run(debug=True)
