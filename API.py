from flask import Flask, jsonify, request

app = Flask(__name__)

# Dữ liệu giả lập
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Web Development", "author": "Jane Smith"},
]

# Lấy danh sách sách
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Lấy thông tin một cuốn sách theo ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Thêm một cuốn sách mới
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    if "title" not in new_book or "author" not in new_book:
        return jsonify({"error": "Invalid input"}), 400
    new_book["id"] = books[-1]["id"] + 1 if books else 1
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# Cập nhật thông tin một cuốn sách
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    updated_data = request.json
    book.update(updated_data)
    return jsonify(book)

# Xóa một cuốn sách
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
