# HNG-12-BE-Stage-0
HNG Internship Backend Track Stage 0 Task

# Flask API with CORS

This Flask app provides a single route (`/api`) that returns a JSON response containing the user's email, GitHub repository URL, and the current time in ISO 8601 format.

## Features

- Single `/api` endpoint that returns JSON.
- CORS enabled for cross-origin requests.
- Current time in ISO 8601 format included in the JSON response.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DavidTimi1/HNG-12-BE-Stage-0.git
   cd your-repository
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app locally:
   ```bash
   python app.py
   ```

2. The app will be available at `http://127.0.0.1:5000/api`. You can test the endpoint using `curl` or Postman.

## Endpoint

### `GET /api`

Returns a JSON response with the following structure:

```json
{
   "email": "duwagbale07@gmail.com",
   "github_url": "https://github.com/DavidTimi1/HNG-12-BE-STAGE-0",
   "current_datetime": "2025-01-30T12:34:56+00:00"
}
```

- `email`: The email address associated with the project.
- `github_url`: URL of the GitHub repository for this project.
- `current_datetime`: Current date and time in ISO 8601 format.

## CORS

CORS (Cross-Origin Resource Sharing) is enabled by default for all routes, allowing the app to be accessed from different origins.

## Dependencies

- Flask
- Flask-Cors

You can install the dependencies using:
```bash
pip install flask flask-cors
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Hire
Wanna see more great backend developers? Click [here](https://hng.tech/hire/python-developers)
