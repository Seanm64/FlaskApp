from flask import Flask, render_template
from data import Ingredients

app = Flask(__name__) #current name for the module


Ingredients = Ingredients()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', ingredients = Ingredients)

    

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True) #debug = true makes it so that you don't have to keep re-running the instance to see changes

