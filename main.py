from flask import Flask, request
from caesar import rotate_string
# , render_template
 
app = Flask(__name__)
app.config['DEBUG'] = True


form ="""
<!DOCTYPE html>
<html>
    <head>
       <style>
       form {
    background-color: #eee;
    padding: 20px;
    margin: 0 auto;
    width: 540px;
    font: 16px sans-serif;
    border-radius: 10px;
}
textarea {
    margin: 10px 0;
    width: 540px;
    height: 120px;
}
       </style>
    </head>
    <body>
      <form action="/" method='POST'>
      <label>Rotate by (input a number)
        <input type=text name="rot" size="5"/>
      </label><br><br>
      <label> Your Message
        <textarea name="text"></textarea>
      </label>
      <input type=submit />
      </form>
    </body>
</html> """

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    txt = request.form['text']
    encrypted_string = rotate_string(txt, rot)
    return f"<h1> {encrypted_string}</h1>"

app.run()