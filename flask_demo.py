from flask import Flask

app = Flask(__name__,)

@app.route('/')
def test():
    
    return "<h1 style='color:green'>Hi hello flask, How are you color changed?</h1>"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')  











