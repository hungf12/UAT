from flask import Flask, jsonify, request
from models2 import db, Item

app = Flask(__name__)

# Cấu hình PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo database
db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# 1. Tạo (Create)
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(
        name=data['name'],
        description=data.get('description'),
        price=data['price']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

# 2. Đọc (Read)
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify(item.to_dict())
    return jsonify({'message': 'Item not found'}), 404

# 3. Cập nhật (Update)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify(item.to_dict())

# 4. Xóa (Delete)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
