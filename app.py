from flask import Flask
app = Flask(__name__)
@app.route('/ak')
def hello_world():
   return  "hello world "


app.run()