from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("saya ganteng.html",saya_ganteng=saya_ganteng)
saya_ganteng = "saya ganteng"

if __name__ == "__main__":
    app.run(debug=True)