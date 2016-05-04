from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def indexhtml():
    return render_template('index.html')

@app.route('/stupid.css')
def stupidcss():
    return render_template('stupid.css')

if __name__=='__main__':
    app.run(port=80, debug = True)
