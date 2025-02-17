from telegram_bot import start_bot
from flask_cors import CORS
from api.api import api
from flask import Flask
import threading
import asyncio

# def run_bot():
#     asyncio.run(start_bot())

# def run_bot():
#     loop = asyncio.new_event_loop()  # Create a new event loop for the thread
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(start_bot())


print("running......")

# def create_app():
    # start_bot()
    
#     app = Flask(__name__)
#     CORS(app)
    
    
#     api.init_app(app)
    
#     return app

def run_flask():
    app = Flask(__name__)
    CORS(app)

    print("Flask app is running...")
    
    api.init_app(app)  # Initialize API if needed
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
    
def main():
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # start_bot()

    # Run Telegram bot in the main thread
    asyncio.run(start_bot())  # Ensure bot runs in main event loop

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     print("running.......")
#     app.run(debug=True, host="0.0.0.0", port=5000)
