
from flask import Flask

# Create our Flask application
app = Flask(__name__)

# Define the home page
@app.route("/")
def home():
    return "<h1>My Finance Tracker</h1><p>Welcome to your personal finance dashboard!</p>"

# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=5001)

