#!/usr/bin/python3

"""
    module to list all the states in the database
"""

import MySQLdb
import sys


def list_states(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306
                )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query to retrieve all states sorted by id
        cursor.execute('SELECT * FROM states ORDER BY id ASC')

        # Fetch all the results
        results = cursor.fetchall()

        # Print the results in the desired format
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        # Close the cursor and connection in a finally block to ensure cleanup
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print('Usage: script.py <username> <password> <database>')
        sys.exit(1)

    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)


if __name__ == '__main__':
    main()
