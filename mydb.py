import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv('dcrm/.env')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = MYSQL_PASSWORD
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")