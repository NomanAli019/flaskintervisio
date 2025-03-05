from flask import Flask, render_template, request, jsonify
from Routes.mainpages_routes import main_pages
from Routes.dashboard_routes import dashboard_pages
from Routes.register_emp import register_user

app = Flask(__name__)

# Home route
app.register_blueprint(main_pages)
app.register_blueprint(dashboard_pages)
app.register_blueprint(register_user)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
