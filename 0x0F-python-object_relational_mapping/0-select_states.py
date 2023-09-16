#!/usr/bin/python3


"""
    module that list all the states in the database
"""

import argparse
import MySQLdb

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='List all states from a MySQL database.')
    parser.add_argument('username', type=str, help='MySQL username')
    parser.add_argument('password', type=str, help='MySQL password')
    parser.add_argument('database', type=str, help='Database name')
    args = parser.parse_args()


    def list_states(username, password, database):

        try:
            connection = MySQLdb.connect(
                    user=username,
                    passwd=password,
                    db=database,
                    host='localhost',
                    port=3306)

            cursor = connection.cursor()

            cursor.execute('SELECT * FROM states ORDER BY id ASC')

            result = cursor.fetchall()

            for ids in result:
                print(ids)

        except MySQLdb.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()


    list_states(args.username, args.password, args.database)

