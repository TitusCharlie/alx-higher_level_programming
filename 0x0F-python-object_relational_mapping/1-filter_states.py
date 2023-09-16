#!/usr/bin/python3


"""
    Module  that lists all states with a name
    starting with N (upper N) from the database
"""


import argparse
import MySQLdb


def list_states(username, password, database):

    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306)

        cursor = connection.cursor()

        cursor.execute(
                'SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC'
                )

        result = cursor.fetchall()

        for name in result:
            print(name)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()


def main():
    parser = argparse.ArgumentParser(
            description='List all states from a MySQL database.')
    parser.add_argument('username', type=str, help='MySQL username')
    parser.add_argument('password', type=str, help='MySQL password')
    parser.add_argument('database', type=str, help='Database name')
    args = parser.parse_args()

    list_states(args.username, args.password, args.database)


if __name__ == '__main__':
    main()
