from flask import Flask
from app.routes.api_routes import api_blueprint

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
