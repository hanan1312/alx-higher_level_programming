#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to a MySQL database then lists all states in 'states' table,
    sorting them by id in ascending order.
    """

    try:
        connection = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
