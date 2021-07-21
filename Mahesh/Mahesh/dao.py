import mysql.connector as connector

config = {
    'user':'webapp',
    'password':'M@hesh57',
    'database':'Mahesh',
}

def get_connection():
    conn = connector.connect(**config)
    return conn

if __name__ == '__main__':
    get_connection()