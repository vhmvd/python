from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def output():
  output = input("Enter string: ")
  return render_template('output.html', result=output)

if __name__=="__main__":
  app.run(debug=True,use_reloader=True)