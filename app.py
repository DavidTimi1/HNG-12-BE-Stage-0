from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
# Initialize CORS
CORS(app)


@app.route('/api', methods=['GET'])
def get_info():
    # Replace the placeholder values below with your actual data
    response = {
        "email": "duwagbale07@gmail.com",  # Your registered Slack email
        "current_datetime": datetime.utcnow().isoformat(),  # Current datetime in ISO 8601 format
        "github_url": "https://github.com/DavidTimi1/HNG-12-BE-Stage-0"  # GitHub repository URL
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
