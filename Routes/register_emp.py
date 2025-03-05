from flask import Blueprint, request, jsonify
from DbOperation.employeeOp import EmployeeOperations

register_user = Blueprint('register_user', __name__)

@register_user.route('/register-employee', methods=['POST'])
def register_emp():
    try:
        request_data = request.get_json()
        print("Request Data:", request_data)  # Debugging log

        data = request_data.get("employeeData", {})
        print("Employee Data:", data)  # Debugging log

        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')
        house_address = data.get('house_address')
        country = data.get('country')

        if not all([full_name, email, password, phone_number, house_address, country]):
            return jsonify({"success": False, "message": "All fields are required"}), 400

        if EmployeeOperations.check_user(email):
            return jsonify({"success": False, "exists": True, "message": "User already exists"}), 400

        EmployeeOperations.create_user(full_name, email, password, phone_number, house_address, country)
        return jsonify({"success": True, "exists": False, "message": "Employee registered successfully!"}), 200

    except Exception as e:
        print("Error:", str(e))  # Debugging log
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500
