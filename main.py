from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def indexhtml():
    return render_template('index.html')

@app.route('/stupid.css')
def stupidcss():
    return render_template('stupid.css')

if __name__=='__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug = True)

