#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get the connection arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, db_name),
        pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database and print the results
    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))

    # Close the session
    session.close()
