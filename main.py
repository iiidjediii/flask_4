
from flask import Flask, render_template, request
from num import searchFib

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
   if request.method == 'POST':
       query = searchFib(int(request.form['query'])) # применяем к числу на входе функцию поиска ближайшего числа Фибоначчи
       return render_template("index.html", value1=query)


if __name__ == "__main__":
    app.run(debug=True)
    
#comment 123