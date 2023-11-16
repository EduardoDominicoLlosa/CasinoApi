RNG API
Welcome to the RNG API, a Flask-based API for managing random number generation.

Overview
The RNG API provides endpoints to retrieve random numbers and add new random number items with customizable modifiers. The API is designed to simulate random number generation with winning odds and jackpot conditions.

Getting Started
Prerequisites
Python 3
Flask (install via pip install flask)
Installation
Clone the repository:

1. Clone the repository:
git clone https://github.com/your-username/rng-api.git
cd rng-api

2. Run the Flask application:
python rng_api.py

3. The API will be accessible at http://127.0.0.1:5000/.

API Endpoints

Get All RNG Items
* URL: /api/rng
* Method: GET
* Description: Retrieve a list of all RNG items.

Add a New RNG Item

* URL: /api/rng
* Method: POST
* Description: Add a new RNG item with customizable modifiers.
To add a new RNG item, you can make a POST request using a tool like `curl`.

>curl -X POST -H "Content-Type: application/json" -d '{"rngModifier": 20}' http://127.0.0.1:5000/api/rng

* -X POST specifies that it's a POST request.
* -H "Content-Type: application/json" sets the content type to JSON.
* -d '{"rngModifier": 20}' provides the JSON data for the new RNG item. Adjust the rngModifier or add any other necessary parameters.
* http://127.0.0.1:5000/api/rng is the URL of the API endpoint.

OR

Making a POST Request with PowerShell.

>$url = "http://127.0.0.1:5000/api/rng"


>$headers = @{
    "Content-Type" = "application/json"
}

>$data = @{
    rngModifier = 20
} | ConvertTo-Json

>Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $data


Response:
>{
    "message": "Data added successfully",
    "rngData": {
        "id": 1,
        "rng": 7,
        "rngModifier": 10,
        "is_jackpot": false,
        "winningOdds": 30.0
    }
}

Customization
* Adjust the rngData array in rng_api.py to customize the initial RNG items.
* Modify the random number generation and winning conditions based on your specific logic.