from flask import Flask, render_template, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def filmes():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)