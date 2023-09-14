import re
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def validate_email(email):
    # Use a regular expression pattern to validate the email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']

    if validate_email(email):
        with open("subscriber_list.txt", "a") as file:
            file.write(email + "\n")
        return 'Thank you for subscribing!'
    else:
        return 'Please enter a valid email address.'

if __name__ == '__main__':
    app.run(debug=True)
