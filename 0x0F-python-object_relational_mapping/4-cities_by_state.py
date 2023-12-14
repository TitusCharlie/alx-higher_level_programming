#!/usr/bin/python3

"""
    Module that lists all cities from the database
    The state each city belong
"""


import argparse
import MySQLdb


def list_cities(username, password, database):

    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306)

        cursor = connection.cursor()

        query = '''SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC'''
        cursor.execute(query)

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

    list_cities(args.username, args.password, args.database)


if __name__ == '__main__':
    main()
