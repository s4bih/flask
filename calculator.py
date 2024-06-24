from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        if operation == "add":
            result = int(num1) + int(num2)
        elif operation == "subtract":
            result = int(num1) - int(num2)
        elif operation == "multiply":
            result = int(num1) * int(num2)
        elif operation == "divide":
            result = int(num1) / int(num2)
        elif operation == "power":
            result = int(num1) * int(num1)
        elif operation == "square":
            result = int(num1) ** (1/2)

        else:
            result = "Invalid operation"

    return render_template("calcullator.html",result = result)




if __name__ == "__main__":
    app.run(debug=True)