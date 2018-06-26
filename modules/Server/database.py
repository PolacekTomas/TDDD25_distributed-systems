# -----------------------------------------------------------------------------
# Distributed Systems (TDDD25)
# -----------------------------------------------------------------------------
# Author: Sergiu Rafiliu (sergiu.rafiliu@liu.se)
# Modified: 24 July 2013
#
# Copyright 2012 Linkoping University
# -----------------------------------------------------------------------------

"""Implementation of a simple database class."""

import random


class Database(object):

    """Class containing a database implementation."""
    databaseArray = []

    def __init__(self, db_file):
        """Initialize the database as an array of strings."""
        try:
            open(db_file)
            self.db_file = db_file
        except Exception as e:
            open(db_file, 'r+')
            print("Could not find database - created database file")
            self.db_file = db_file
        self.rand = random.Random()
        self.rand.seed()
        with open(self.db_file) as file:
            result = []
            read_line = ""
            for line in file:
                if ('%\n' in line and len(line) == 2) or ('%' in line and len(line) == 1) :
                    result.append(read_line)
                    read_line = ""
                else:
                    read_line += line
            self.databaseArray = result;

    def read(self):
        """Read a random location in the database."""
        if len(self.databaseArray) == 0:
            return "Database is empty - write something with w <fortune>"
        rand = random.randrange(0, len(self.databaseArray))
        return self.databaseArray[rand]

    def write(self, fortune):
        """Write a new fortune to the database."""
        self.databaseArray.append(fortune)
        #open file in append mode
        db_file = open(self.db_file, "a")
        db_file.write(fortune + "\n%\n")
        db_file.close()
