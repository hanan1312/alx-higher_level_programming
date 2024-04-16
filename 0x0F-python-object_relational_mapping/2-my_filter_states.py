#!/usr/bin/python3
""" 2 filter states """

import MySQLdb
import sys

def list_states(username, password, database, search_name):
    """
    Connects to a MySQL database and lists all states from the 'states' table,
    matching the provided search_name, sorting them by id in ascending order.
    """

    try:
        connection = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
        cursor = connection.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cursor.execute(query, (search_name,))

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <search_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    list_states(username, password, database, search_name)
