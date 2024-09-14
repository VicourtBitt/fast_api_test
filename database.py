import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Função para conectar ao banco de dados
def connect():
    return mysql.connector.connect(
        host= 'localhost',
        user= os.getenv('MYSQL_USER'),
        password= os.getenv('MYSQL_PASS'),
        database= 'gc2024'
    )