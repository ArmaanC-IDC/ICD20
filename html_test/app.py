from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Data dynamically retrieved from somewhere (e.g., a database)
    user = {'username': 'John', 'email': 'john@example.com'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)
