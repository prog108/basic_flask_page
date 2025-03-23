from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=[ 'GET','POST']) 
def index():
    ispis = ''
    if request.method == 'POST':
        ispis = request.form['input_text']
    return render_template('index.html', output=ispis)

@app.route('/o-projektu') 
def o_nama():
    return render_template('o_projektu.html')

if __name__ == '__main__':
    app.run(debug=True)
