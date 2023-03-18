#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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

    # Query the database and delete the State objects
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
