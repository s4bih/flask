from flask import Flask,render_template
app = Flask(__name__)


book = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year': 1925

    },



    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1960

    }
]
title = "My First Flask App"
@app.route("/")
def hello_world():
    return render_template("index.html",Title=title,book=book)

@app.route("/books/<int:book_id>")
def get_book(book_id):
    pass



if __name__ == "__main__":
    app.run(debug=True)










































































































































































