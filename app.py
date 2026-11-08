
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return """
    <h1>Welcome to Recruitment System</h1>
    <p>Our recruitment website is running successfully.</p>
    """

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
  