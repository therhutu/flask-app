from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Rhutu')

if __name__=='__main__':
    app.run(debug=True)

