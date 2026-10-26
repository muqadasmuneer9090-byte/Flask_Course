from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    first_name = "suman"
    last_name = "muneer"
    course = [
        "python",
        "flask",
        "html",
        "css",
        "javascript"
    ]
    city = "khuzdar"
    age  = 23
    return render_template("index.html", first_name=first_name,     last_name=last_name,  course=course, city=city, age=23)

if __name__ == "__main__":
    app.run(debug=True)