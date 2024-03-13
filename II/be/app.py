from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2

app = Flask(__name__)
cors = CORS(app)

def get_db_connection():
    return psycopg2.connect(host="db-psql", database="books", user="postgres", password="mysecretpassword")

@app.route("/books", methods=['GET'])
@cross_origin()
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM book;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    books_dict = [{'id': book[0], 'title': book[1], 'author': book[2]} for book in books]

    return jsonify(books_dict)

@app.route("/books/<int:book_id>", methods=['GET'])
@cross_origin()
def get_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE id=%s;', (book_id,))
    book = cur.fetchall()
    cur.close()
    conn.close()
    if len(book) != 0:
        return jsonify({'id': book[0][0], 'title': book[0][1], 'author': book[0][2]})
    return {'error': 'Book not found'}

@app.route("/books", methods=['POST'])
@cross_origin()
def insert_book():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO book (title, author)'
            'VALUES (%s, %s)',
            (request.json['title'],
             request.json['author'])
            )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': 1, 'title': request.json['title'], 'author': request.json['author']})



@app.route("/books/<int:book_id>", methods=['PUT'])
@cross_origin()
def update_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=%s, author=%s WHERE id=%s;',
            (request.json['title'],
             request.json['author'],
             book_id))

    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': book_id, 'title': request.json['title'], 'author': request.json['author']})


@app.route("/books/<int:book_id>", methods=['DELETE'])
@cross_origin()
def delete_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id=%s;',
            (book_id,))
    conn.commit()
    cur.close()
    conn.close() 
    return jsonify({'id': book_id})


if __name__ == "__main__":
    app.run(debug=True)
