from flask_cors import CORS
from flask import Flask
from api.api import api
from telegram_bot import start_bot

def create_app():
    start_bot()
    
    app = Flask(__name__)
    CORS(app)
    
    print("running......")
    
    api.init_app(app)
    
    return app

# if __name__ == "__main__":
#     print("running.......")
#     app.run(debug=True, host="0.0.0.0", port=5000)
