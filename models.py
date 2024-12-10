from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

# Định nghĩa model (bảng Book trong database)
class Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
# định nghĩa bảng thông tin hợp đồng
class Infomation_contract(db.Model):
    pol_id = db.Column(db.String(100), primary_key=True)
    due_date = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    prd_type = db.Column(db.String(100), nullable=False)
