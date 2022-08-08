from flask import Flask
app=Flask(__name__)

@app.route('/')
def default():
    return 'My default API'


if __name__=="__main__":
    app.run(debug=True)
