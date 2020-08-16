# 连接数据可以
from flask import Flask

HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'student'
db_url = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICATIONS = False