from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/intervisio_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)  # Store hashed passwords!
    phone_number = db.Column(db.String(50), nullable=False)
    house_address = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Employee {self.full_name}>"

# Run this to create tables only once
if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        print("Tables created successfully in intervisio_db!")
