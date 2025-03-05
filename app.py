from flask import Flask, render_template, request, jsonify
from Routes.mainpages_routes import main_pages

app = Flask(__name__)

# Home route
app.register_blueprint(main_pages)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
