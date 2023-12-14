#!/usr/bin/python3

"""
    Module that correct sql injection following
    module 2 script
"""


import argparse
import MySQLdb


def list_states(username, password, database, state_name):

    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306)

        cursor = connection.cursor()

        query = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'
        cursor.execute(query, (state_name,))

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
    parser.add_argument('state_name', type=str, help='State name')
    args = parser.parse_args()

    list_states(args.username, args.password, args.database, args.state_name)


if __name__ == '__main__':
    main()
