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
