import os
from flask import Flask
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
