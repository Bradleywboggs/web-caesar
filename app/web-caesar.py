from flask import Flask, request, render_template
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    txt = request.form['text']
    encrypted_string = rotate_string(txt, rot)
    return render_template("form.html", text=encrypted_string)


app.run()
