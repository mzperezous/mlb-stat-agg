"""
    Collection of DB helper functions.
"""

import getopt
import psycopg2 as psql


def execute_single_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
    return


def get_connection(argvec):
    # Get credentials from specified file
    cred_file = ".cred-local"
    try:
        options, args = getopt.getopt(argvec, 'c', ['credentials='])
        for opt, arg in options:
            if opt in ('-c', '--credentials'):
                cred_file = str(arg)

    except getopt.GetoptError:
        error_message = "Usage: create_master_tables.py [-c | --credentials cred]\n"
        error_message += "\t-c or --credentials\n\t\t cred: Path to credentials file\n"
        raise getopt.GetoptError(error_message)

    # Pull credentials
    connection_data = None
    try:
        with open(cred_file, "r") as f:
            connection_data = f.read()
            print(connection_data)
    except Exception:
        raise OSError(f'Couldn\'t open credentials file at {cred_file}')

    # Get and return connection to the specified DB
    try:
        return psql.connect(connection_data)
    except Exception:
        raise OperationalError("Couldn't establish connection to database.")
