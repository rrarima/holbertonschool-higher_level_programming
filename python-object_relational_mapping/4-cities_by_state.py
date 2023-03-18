#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name\
             FROM cities\
             JOIN states ON cities.state_id = states.id\
             ORDER BY cities.id"\

    #name = (sys.argv[4],)

    # Execute SQL query to fetch all the states in the database
    cursor.execute(query)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
