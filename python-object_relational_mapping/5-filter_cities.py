#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
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

    query = "SELECT cities.id, cities.name, states.name \
             FROM states, cities \
             WHERE cities.state_id = states.id \
             AND states.name = %s \
             ORDER BY cities.id"

    name = sys.argv[4],

    # Execute SQL query to fetch all the states in the database
    cursor.execute(query, name)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    cities = ", ".join([row[1] for row in rows])
    print(cities)

    # Close cursor and database connection
    cursor.close()
    db.close()
