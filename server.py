import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

# Route for the Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the Course Overview Page
@app.route('/course')
def course():
    return render_template('course.html')

# Routes for each individual Learning Module
@app.route('/module/1')
def module1():
    return render_template('module1.html')

@app.route('/module/2')
def module2():
    return render_template('module2.html')

@app.route('/module/3')
def module3():
    return render_template('module3.html')

@app.route('/module/4')
def module4():
    return render_template('module4.html')

# Route for the About Us Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Feedback Page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    # Flask port is 8080 by default for Google Cloud Run
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
