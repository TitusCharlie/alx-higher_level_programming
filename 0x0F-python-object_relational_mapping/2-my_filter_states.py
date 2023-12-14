#!/usr/bin/python3


"""
    Module that takes in an argument
    displays all values in the states table of database
    where name matches the argument
"""


import argparse
import MySQLdb


def filter_states(username, password, database, state_name):

    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                )

        cursor = connection.cursor()

        query = """ SELECT * FROM states
          WHERE name LIKE '{}'
          ORDER BY id ASC """.format(state_name,)

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
    parser.add_argument('state_name', type=str, help='State name')
    args = parser.parse_args()

    filter_states(args.username, args.password, args.database, args.state_name)


if __name__ == '__main__':
    main()
