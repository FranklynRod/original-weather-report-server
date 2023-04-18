# original-weather-report-server

The Original Weather Report proxy server is to be used with the [Original Weather Report web app project](https://github.com/FranklynRod/weather-report)**

#### Package Manager
1. Create and activate a virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
2. Install the `requirements.txt`
    - `pip install -r requirements.txt`
    - `pip freeze > requirements.txt` add updated requirement to requirements.txt file
3. Run the server
    - `FLASK_ENV=development flask run`
