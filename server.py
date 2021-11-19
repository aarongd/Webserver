from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    print(url_for('static', filename='bonefire.cio'))
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'These are my thoughts'

@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'