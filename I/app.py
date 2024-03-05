from flask import Flask, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Zlocin i kazna", "author": "F.M. Dostojevski"},
    {"id": 2, "title": "Sofijin svet", "author": "Justejn Gorder"},
    {"id": 3, "title": "Ohridski prolog", "author": "Vladika Nikolaj Velimirovic"},
    {"id": 4, "title": "Gubiliste", "author": "Cingiz Ajtmatov"}
]

@app.route("/books", methods=['GET'])
def get_books():
    return books

@app.route("/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    for book in books: 
        if book["id"] == book_id:
            return book
    return {'error': 'Book not found'}

@app.route("/books", methods=['POST'])
def insert_book():
    new_book =  {
            'id': len(books) + 1,
            'title': request.json['title'],
            'author': request.json['author'],
        }
    books.append(new_book)
    return new_book


@app.route("/books/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    for book in books: 
        if book["id"] == book_id:
            book["title"] = request.json['title']
            book["author"] = request.json['author']
            return book
    return {'error': 'Book not found'}

@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    for book in books: 
        if book["id"] == book_id:
            books.remove(book)
            return {"response": "Book deleted"}

    return {'error': 'Book not found'}

if __name__ == "__main__":
    app.run(debug=True)
