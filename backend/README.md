# Back-end API

The backend API is responsible for handling all the server-side logic and data processing for Prophet forecasting model application. It provides endpoints for forecasting and authentication. The API is built using Flask.

## Installation
1. Create a virtual environment using the following command:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. install psycopg2
```bash
sudo apt-get install libpq-dev python3-dev python3-psycopg2
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

5. Create a `backend/.env` file:
```bash
cp .env.example .env
```

6. Run the application:
```bash
python app.py
```

7. The application will be running on `http://localhost:5000/`


