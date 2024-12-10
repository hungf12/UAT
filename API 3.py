from flask import Flask, jsonify, request
from models import db, Information, Infomation_contract

app = Flask(__name__)

# Cấu hình SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo database
db.init_app(app)

# Tạo database nếu chưa tồn tại
with app.app_context():
    db.create_all()


# New Enpoint: tạo thêm thông tin hợp đồng
@app.route('/Create-contract', methods=['POST'])
def add_contract():
    data = request.json

    # Kiểm tra nếu request rỗng
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # # Kiểm tra nếu thiếu trường 'title' hoặc 'author'
    # if "identification" not in data or "name" not in data or "date" not in data or "location" not in data:
    #     return jsonify({"error": "Invalid input: 'title' and 'author' are required"}), 400
    #
    # # Kiểm tra nếu 'title' hoặc 'author' là chuỗi rỗng
    if not data.get('pol_id') or not data.get('due_date') or not data.get('price') or not data.get('prd_type'):
        return jsonify({"error": "All fields (identification, name, date, location) must be provided and cannot be empty"}), 400

    # Kiểm tra dữ liệu trùng lặp trong database
    existing_infors_contract = Infomation_contract.query.filter_by(pol_id=data['pol_id'], due_date=data['due_date'], price=data['price'], prd_type=data['prd_type']).first()
    if existing_infors_contract:
        return jsonify({"error": "Duplicate entry: Information with the same identification, name date and location already exists"}), 409

    # Nếu không có lỗi, thêm sách mới vào database
    new_info = Infomation_contract(pol_id=data['pol_id'], due_date=data['due_date'], price=data['price'], prd_type=data['prd_type'])
    db.session.add(new_info)
    db.session.commit()
    return jsonify({
        "message": "Create Information Contract successfully",
        "Data": {"pol_id": new_info.pol_id, "due_date": new_info.due_date, "price": new_info.price, "prd_type": new_info.prd_type}
    }), 200

#New enpoint: lấy thông tin hợp đồng trong database
@app.route('/contract', methods=['GET'])
def get_contract():
    get_info_contract = Infomation_contract.query.all()
    result = [{"pol_id": information_contract.pol_id, "due_date": information_contract.due_date, "price": information_contract.price, "prd_type": information_contract.prd_type} for information_contract in get_info_contract]
    return jsonify(result)
#new enpoint: lấy thông tin trong hợp đông qua mã hợp đồng
@app.route('/contract/<string:contract_id>', methods=['GET'])
def get_contract_id(contract_id):
    contract_id = Infomation_contract.query.get(contract_id)
    if not contract_id:
        return jsonify({"error": "No contract information found"}), 400
    return jsonify({
        "message": "Find contract information successfully",
        "Data": {"due_date": contract_id.due_date, "price": contract_id.price, "prd_type": contract_id.prd_type}
    })
if __name__ == '__main__':
    app.run(debug=True)
