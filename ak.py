from flask import Flask
app = Flask(__name__)
f=open("s.html")
str=f.read()
print(str)
@app.route('/')
def hello_world():
   return  str

if __name__ == '__main__':
   app.run()