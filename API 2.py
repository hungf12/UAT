from flask import Flask, jsonify, request
from models import db, Information

app = Flask(__name__)

# Cấu hình SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo database
db.init_app(app)

# Tạo database nếu chưa tồn tại
with app.app_context():
    db.create_all()

# Endpoint: Lấy danh sách sách
@app.route('/infors', methods=['GET'])
def get_books():
    infors = Information.query.all()
    result = [{"id": information.id, "identification": information.identification, "name": information.name, "date": information.date, "location": information.location} for information in infors]
    return jsonify(result)

# Endpoint: Lấy thông tin một cuốn sách theo ID
@app.route('/infors/<int:info_id>', methods=['GET'])
def get_book(info_id):
    infor_id = Information.query.get(info_id)
    if not infor_id:
        return jsonify({"error": "Information not found"}), 404
    return jsonify({"id": infor_id.id, "identification": infor_id.identification, "name": infor_id.name})

# Endpoint: Thêm sách mới
@app.route('/Create-infors', methods=['POST'])
def add_book():
    data = request.json

    # Kiểm tra nếu request rỗng
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # # Kiểm tra nếu thiếu trường 'title' hoặc 'author'
    # if "identification" not in data or "name" not in data or "date" not in data or "location" not in data:
    #     return jsonify({"error": "Invalid input: 'title' and 'author' are required"}), 400
    #
    # # Kiểm tra nếu 'title' hoặc 'author' là chuỗi rỗng
    if not data.get('identification') or not data.get('name') or not data.get('date') or not data.get('location'):
        return jsonify({"error": "All fields (identification, name, date, location) must be provided and cannot be empty"}), 400

    # Kiểm tra dữ liệu trùng lặp trong database
    existing_infors = Information.query.filter_by(identification=data['identification'], name=data['name'], date=data['date'], location=data['location']).first()
    if existing_infors:
        return jsonify({"error": "Duplicate entry: Information with the same identification, name date and location already exists"}), 409

    # Nếu không có lỗi, thêm sách mới vào database
    new_info = Information(identification=data['identification'], name=data['name'], date=data['date'], location=data['location'])
    db.session.add(new_info)
    db.session.commit()
    return jsonify({
        "message": "Create Information successfully",
        "Data": {"id": new_info.id, "identification": new_info.identification, "name": new_info.name, "date": new_info.date, "location": new_info.location,}
    }), 200


# Endpoint: Cập nhật thông tin sách
@app.route('/infors/<int:info_id>', methods=['PUT'])
def update_book(info_id):
    infor_id = Information.query.get(info_id)
    if not infor_id:
        return jsonify({"error": "Book not found"}), 404
    data = request.json
    if "identification" in data:
        infor_id.identification = data['identification']
    if "name" in data:
        infor_id.name = data['name']
    db.session.commit()
    return jsonify({"message": "Information updated successfully", "Data": {"id": infor_id.id, "identification": infor_id.identification, "name": infor_id.name}})

# Endpoint: Xóa sách
@app.route('/books/<int:info_id>', methods=['DELETE'])
def delete_book(info_id):
    infor_id = Information.query.get(info_id)
    if not infor_id:
        return jsonify({"error": "Information not found"}), 404
    db.session.delete(infor_id)
    db.session.commit()
    return jsonify({"message": "Information deleted successfully"})

# Endpoint: Kiểm tra và trả về thông tin dựa trên 'identification'
@app.route('/infors/check_identification', methods=['POST'])
def check_identification():
    data = request.json

    # Kiểm tra xem có dữ liệu identification trong request không
    if 'identification' not in data:
        return jsonify({"error": "Identification is required"}), 400

    identification = data['identification']

    # Tìm thông tin dựa trên identification
    infor = Information.query.filter_by(identification=identification).first()

    if not infor:
        return jsonify({"error": "Identification not found"}), 404

    # Trả về thông tin name, date, location
    return jsonify({"message":"Search data successfully", "Data": {
        "identification": infor.identification,
        "name": infor.name,
        "date": infor.date,
        "location": infor.location
    }})


if __name__ == '__main__':
    app.run(debug=True)
