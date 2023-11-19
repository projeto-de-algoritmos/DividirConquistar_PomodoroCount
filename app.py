from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", work_time=25 * 60, break_time=5 * 60)

if __name__ == "__main__":
    app.run(debug=True)
