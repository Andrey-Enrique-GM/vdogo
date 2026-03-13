import pymysql

def get_connection():
    pymysql.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "dogodb"
    )