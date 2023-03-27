import mysql.connector
import os

"""db = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)"""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)
def get_db():
    return db
