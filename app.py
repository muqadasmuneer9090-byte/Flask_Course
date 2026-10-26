from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "suman"
    course = "Flask"
    city = "khuzdar"
    age  = 23
    return render_template("index.html", name=name, course=course, city=city, age=23)

if __name__ == "__main__":
    app.run(debug=True)