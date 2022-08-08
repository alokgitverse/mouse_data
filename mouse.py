from flask import Flask
app=Flask(__name__)

@app.route('/')
def default():
    return 'My default API'

@app.route('/my_name')
def my_name():
    return "Alok Kumar DAs"


if __name__=="__main__":
    app.run(debug=True)
