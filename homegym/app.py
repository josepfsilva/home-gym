from flask import Flask, render_template
from views import mgvideos, mgamificacao, mgamigos, mgtreinos

app = Flask(__name__)
#app.config.from_object('config.py')

@app.route("/")
def open()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)