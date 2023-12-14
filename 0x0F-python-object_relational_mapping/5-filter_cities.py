#!/usr/bin/python3

"""
    Module that takes in the name of a state as an argument
    list all cities of that state, using the database
"""


import argparse
import MySQLdb


def list_cities(username, password, database, state_name):

    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306)

        cursor = connection.cursor()

        query = '''SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC'''
        cursor.execute(query, (state_name,))

        result = cursor.fetchall()

        city_name = [', '.join(name) for name in result]
        print(', '.join(city_name))

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
    parser.add_argument('state_name', type=str, help='State name')
    args = parser.parse_args()

    list_cities(args.username, args.password, args.database, args.state_name)


if __name__ == '__main__':
    main()
