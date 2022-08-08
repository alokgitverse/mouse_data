from flask import Flask
app=Flask(__name__)

@app.route('/')
def default():
    return 'My default API'

@app.route('/my_name')
def my_name():
    return "ALOK KUMAR DAS"


if __name__=="__main__":
    app.run(debug=True)
