from flask import Flask
from app.routes.api_routes import api_blueprint
import os

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    # Bind to the specified PORT environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
